"""
Project 2: Expense Tracker
Author: Mahnoor Saghir
DecodeLabs - Python Programming (Industrial Training Kit, Batch 2026)

What this program does:
  - Keeps asking the user for expenses inside a continuous loop.
  - Adds every valid expense to a running total (accumulator pattern).
  - Rejects invalid input (text, negative numbers, zero) without crashing.
  - Lets the user type commands: 'show' (see history) and 'quit' (stop).
  - Prints a final summary when the program ends.

Follows the IPO model:  INPUT -> PROCESS -> OUTPUT
"""

from decimal import Decimal, InvalidOperation  # Decimal = exact money math (no 0.1 + 0.2 bugs)

# --------------------------------------------------------------------------
# STATE (memory of the program)
# These are created OUTSIDE the loop. If they were inside, they would reset
# to zero on every iteration and the program would "forget" old expenses.
# --------------------------------------------------------------------------
total = Decimal("0")   # accumulator: running total of all expenses
expenses = []          # history: every valid expense is stored here

# Special words the user can type instead of an amount (sentinel values)
QUIT_COMMAND = "quit"
SHOW_COMMAND = "show"


def show_welcome():
    """Print the welcome banner and instructions."""
    print("=" * 45)
    print("          EXPENSE TRACKER")
    print("=" * 45)
    print("Enter an expense amount, e.g. 100, 50, 20.5")
    print(f"Type '{SHOW_COMMAND}' to see all expenses so far.")
    print(f"Type '{QUIT_COMMAND}' to finish and see the total.")
    print("-" * 45)


def show_history():
    """Display every expense entered so far with the running total."""
    if not expenses:
        print("  No expenses recorded yet.")
        return

    print("\n  --- Expense History ---")
    for number, amount in enumerate(expenses, start=1):
        print(f"  {number}. ${amount:.2f}")
    print(f"  Running total: ${total:.2f}\n")


def show_summary():
    """Print the final report. This is the OUTPUT phase."""
    print("\n" + "=" * 45)
    print("            FINAL SUMMARY")
    print("=" * 45)

    if not expenses:
        print("No expenses were entered.")
    else:
        count = len(expenses)
        average = total / count
        print(f"Number of expenses : {count}")
        print(f"Highest expense    : ${max(expenses):.2f}")
        print(f"Lowest expense     : ${min(expenses):.2f}")
        print(f"Average expense    : ${average:.2f}")

    # The most important line of the project
    print(f"\nFINAL TOTAL: ${total:.2f}")
    print("=" * 45)


# --------------------------------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------------------------------
show_welcome()

while True:  # continuous audit loop - runs until the user types 'quit'

    # ---------------- INPUT: the gate ----------------
    # input() always returns TEXT (a string), never a number.
    # .strip() removes extra spaces, .lower() makes 'QUIT' and 'quit' the same.
    entry = input("Enter expense: ").strip().lower()

    # ---------------- Kill switch (sentinel value) ----------------
    if entry == QUIT_COMMAND:
        break  # leave the loop gracefully

    # Show history command: display it, then ask again
    if entry == SHOW_COMMAND:
        show_history()
        continue  # skip the rest and go back to the top of the loop

    # ---------------- Defensive coding: the gatekeeper ----------------
    # Convert text to a number. If it is not a valid number
    # (e.g. "ten" or empty), Decimal raises InvalidOperation.
    try:
        new_expense = Decimal(entry)
    except InvalidOperation:
        print("  Invalid Data: please enter a number like 100 or 25.50.")
        continue

    # Extra validation: nan / infinity are technically "numbers" to Decimal
    # but make no sense as money, so we block them.
    if not new_expense.is_finite():
        print("  Invalid Data: that is not a real amount.")
        continue

    # Business rule: an expense must be a positive amount
    if new_expense <= 0:
        print("  Expense must be greater than zero.")
        continue

    # ---------------- PROCESS: the engine ----------------
    # Accumulator pattern: new state = old state + input
    total += new_expense
    expenses.append(new_expense)  # remember it for the history/summary

    print(f"  Added ${new_expense:.2f}  |  Total so far: ${total:.2f}")

show_summary()
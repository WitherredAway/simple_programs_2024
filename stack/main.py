TOP = -1


def is_empty(stack):
    """Return True if the stack is empty, otherwise False"""

    return stack == []


def push(stack, item):
    """Add an item to the top of the stack"""

    stack.append(item)


def pop(stack):
    """Remove the top item of the stack"""

    if is_empty(stack):
        return False

    return stack.pop()


def peek(stack):
    """View the top item of the stack"""

    if is_empty(stack):
        return False

    return stack[TOP]


def display(stack):
    """View all items of the stack"""

    if is_empty(stack):
        return False

    print(stack[TOP], "<-- Top")
    for i in stack[TOP - 1 :: -1]:
        print(i)
    print("End of items")


stack = []
while True:
    try:
        print(
            f"""
+================================================+
|                Stack Operations                |
+------------------------------------------------+
1. Push - {push.__doc__}
2. Pop - {pop.__doc__}

3. Peek - {peek.__doc__}
4. Display - {display.__doc__}

5. Exit
=================================================="""
        )

        try:
            option = int(input("Please choose an option 1-5: "))
        except ValueError:
            print("Invalid input, must be an integer.")
            continue

        print()

        if option == 1:
            item = input("Please input item to push to stack: ")
            push(stack, item)
            print(f"Successfully pushed `{item}` to stack.")
            continue

        elif option == 2:
            popped = pop(stack)
            if popped is False:
                print("Stack empty.")
                continue

            print(f"Popped item `{popped}` from the stack.")
            continue

        elif option == 3:
            top_item = peek(stack)
            if top_item is False:
                print("Stack Empty.")
                continue

            print(f"The top item of the stack is `{top_item}`.")
            continue

        elif option == 4:
            displayed = display(stack)
            if displayed is False:
                print("Stack Empty.")
                continue

            continue

        elif option == 5:
            print("Exited.")
            break

    except KeyboardInterrupt:
        print("\n\nExited.")
        break

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max_size 5

int stack[max_size], top = -1;

void push();
void pop();
void display();
void pali();

int main()
{
    int choice;

    while (1)
    {
        printf("\n ----Stack operations----\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Palindrome\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            push();
            break;

        case 2:
            pop();
            break;

        case 3:
            // pali();
            break;

        case 4:
            display();
            break;

        case 5:
            exit(0);

        default:
            printf("\n Invalid choice: \n");
            break;
        }
    }
    return 0;
}

void push()
{
    int item;
    if (top == (max_size - 1))
    {
        printf("\n Stack overflow\n");
    }
    else
    {
        printf("Enter the element: ");
        scanf("%d", &item);
        top++;
        stack[top] = item;
    }
}

void pop()
{
    int item;

    if (top == -1)
    {
        printf("Stack is Underflow\n");
    }
    else
    {
        item = stack[top];
        top--;
        printf("The element popped is: %d\n", item);
    }
}

void display()
{
    int i;

    if (top == -1)
    {
        printf("Stack is Underflow\n");
    }
    else
    {
        printf("The elements are:\n");

        for (i = top; i >= 0; i--)
        {
            printf("%d\n", stack[i]);
        }
    }
}

// void pali()
// {
//     int i, j, len = top + 1;
//     int isPalindrome = 1;

//     // Check for palindrome
//     for (i = 0, j = len - 1; i < j; i++, j--)
//     {
//         if (stack[i] != stack[j])
//         {
//             isPalindrome = 0;
//             break;
//         }
//     }

//     if (isPalindrome)
//     {
//         printf("The stack elements form a palindrome.\n");
//     }
//     else
//     {
//         printf("The stack elements do not form a palindrome.\n");
//     }
// }

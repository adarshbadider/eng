#include <stdio.h>
#include <stdlib.h>

#define max 4

int q[max], f = -1, r = -1;

void ins() {
    if ((r + 1) % max == f) {
        printf("\n Queue overflow");
    } else {
        if (f == -1)
            f = 0;
        r = (r + 1) % max;
        printf("\n Enter element to be inserted: ");
        scanf("%d", &q[r]);
    }
}

void del() {
    if (f == -1) {
        printf("\n Queue underflow");
    } else {
        printf("\n Elem deleted is %d", q[f]);
        if (f == r)
            f = r = -1;
        else
            f = (f + 1) % max;
    }
}

void disp() {
    if (f == -1)
        printf("\n Queue Empty");
    else {
        int i;
        printf("\n Queue elements are:\n");
        for (i = f; i != r; i = (i + 1) % max)
            printf("%d\t", q[i]);
        printf("%d\n", q[i]);
        printf("Front is at: %d\nRear is at: %d", q[f], q[r]);
    }
}

int main() {

    int ch;
    while (1) {
    printf("\n Circular Queue operations");
    printf("\n 1. Insert");
    printf("\n 2. Delete");
    printf("\n 3. Display");
    printf("\n 4. Exit");
        printf("\n Enter choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                ins();
                break;
            case 2:
                del();
                break;
            case 3:
                disp();
                break;
            case 4:
                exit(0);
            default:
                printf("\n Invalid choice---!");
        }
    }
    return 0;
}

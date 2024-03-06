#include <stdio.h>

// Function to check if a substring matches the pattern
int matchPattern(const char *str, const char *pattern) {
    while (*pattern) {
        if (*str != *pattern)
            return 0;
        str++;
        pattern++;
    }
    return 1;
}

// Function to replace the pattern with replacement string
void replacePattern(char *str, const char *pattern, const char *replace) {
    int patternLen = 0;
    int replaceLen = 0;

    // Calculate lengths of pattern and replacement string
    while (pattern[patternLen])
        patternLen++;
    while (replace[replaceLen])
        replaceLen++;

    // Loop through the string
    while (*str) {
        // If pattern matches at the current position
        if (matchPattern(str, pattern)) {
            // Replace the pattern with the replacement string
            for (int i = 0; i < replaceLen; i++)
                *(str + i) = replace[i];
            // Shift the rest of the string to the left
            for (int i = replaceLen; *(str + i); i++)
                *(str + i) = *(str + i + patternLen - replaceLen);
            // Move the pointer to the end of the replacement
            str += replaceLen;
        } else {
            // Move to the next character
            str++;
        }
    }
}

int main() {
    char str[100];
    char pattern[50];
    char replace[50];

    // Input string, pattern, and replacement string
    printf("Enter a string: ");
    gets(str); // Note: gets() is unsafe, but used for simplicity
    printf("Enter pattern string: ");
    gets(pattern);
    printf("Enter replacement string: ");
    gets(replace);

    // Perform pattern matching and replacement
    replacePattern(str, pattern, replace);

    // Output the modified string
    printf("Result: %s\n", str);

    return 0;
}

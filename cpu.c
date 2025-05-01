#include <stdlib.h>
#include <stdio.h>

char* run_cpu(char** instructions) {
    for (int i = 0; i < 100; i++) {
        if (instructions[i] == "END") {
            printf("Program ended\n");
            return 0;
        } else {
            printf("%s, ", instructions[i]);
        }
    }
    // printf("%s", instructions[1]);
    return 0;
}

int main() {
    char* test_arr[] = {"LOAD x", "test complete", "test", "END"};
    run_cpu(test_arr);
    return 0;
}
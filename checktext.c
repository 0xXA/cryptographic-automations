#include <stdio.h>
#include <string.h>

void populate_frequencies(int *freq_table, const char *str) {
    for (int i = 0; i <= strlen(str) - 1; ++i)
        ++freq_table[str[i] - 0x41];
}

double index_of_coincidence(int *freq_table, const char* str) {
    double ic = 0;

    for (int i = 0; i < 26; ++i)
        ic += freq_table[i] * freq_table[i];
    ic /= (strlen(str) * strlen(str));
    return ic;
}

int main(int argc, char *argv[]) {
	int freq_table[26];
    double ic = 0;

    if (argc < 2) {
        fprintf(stderr, "Argument expected %s \"Text here\"\n",argv[0]);
        return -1;
    }
    memset(freq_table, 0, 26*sizeof(int));
    populate_frequencies(freq_table, argv[1]);
    ic = index_of_coincidence(freq_table, argv[1]);
    printf("IC=%f",ic);

    return 0;
}
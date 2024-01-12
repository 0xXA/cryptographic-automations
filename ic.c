#include <stdio.h>
#include <string.h>

void populate_frequencies(int *freq_table, const char *str) {
    for (int i = 0; i <= strlen(str) - 1; ++i)
        ++freq_table[str[i] - 0x41];
}

double index_of_coincidence(int *freq_table, const char* str) {
    double ic = 0;

    for (int i = 0; i < 26; ++i)
        ic += freq_table[i] * (freq_table[i] - 1);
    ic /= (strlen(str) * (strlen(str) - 1));
    return ic;
}

int main(int argc, char *argv[]) {
	char buff[500];
	int freq_table[26];
	FILE *inf = fopen("ic_ip.txt","r");
	FILE *outf = fopen("ic_op.txt", "w");

	while(fscanf(inf, "%s", buff)!=EOF) {
    	memset(freq_table, 0, 26*sizeof(int));
    	populate_frequencies(freq_table, buff);
    	fprintf(outf,"string: %s, IC=%f\n", buff, index_of_coincidence(freq_table, buff));
    }
    fclose(inf);
    fclose(outf);

    return 0;
}
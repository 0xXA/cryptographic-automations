#include <stdio.h>
#include <string.h>

void populate_frequencies(int *freq_table, const char *str) {
    for (int i = 0; i <= strlen(str) - 1; ++i)
        ++freq_table[str[i] - 0x41];
}

int main(int argc, char *argv[]) {
    char buff[500];
	int freq_table[26];
	FILE *inf = fopen("ic_ip.txt","r");
	FILE *outf = fopen("freq_table.txt", "w");

	while(fscanf(inf, "%s", buff)!=EOF) {
    	memset(freq_table, 0, 26*sizeof(int));
    	populate_frequencies(freq_table, buff);
        fprintf(outf,"\tfi\n----------\n");
        for(int i=0;i<26;++i)
            fprintf(outf,"%c\t%d\n", i+0x41, freq_table[i]);
        fprintf(outf,"\nnumber of letters, n = %d\n", strlen(buff));
    }
    fclose(inf);
    fclose(outf);

    return 0;
}
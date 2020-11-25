#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 128
#define SUCCESS 1
#define FAIL 0
#define DATA_LEN 20000
#define KEY_LEN 64
#define DIGITS 512
#define BASE 128

int W[KEY_LEN+1][DIGITS];
int key[KEY_LEN];
unsigned char buf1[DATA_LEN], buf2[DATA_LEN];

void add(int *A, int *B){
    int carry = 0;
    int i;
    int x;

    for(i=0;i<256;i++){
        x = A[i]+B[i]+carry; 
        carry = x / MAX; 
        A[i] = x % MAX; 
    }
}

void my_error(void){
    puts("something wrong");
    exit(0);
}

int main(int argc, char* argv[]){
    if(argc != 3){
        puts("CyKorPath.exe <public key> <private key>");
        return 0;
    }

    FILE *fp = fopen(argv[1], "r");
    if(fp == NULL)  my_error();

    fread(buf1, 1, DATA_LEN, fp);
    fclose(fp);

    fp = fopen(argv[2], "r");
    if(fp == NULL)  my_error();

    fread(buf2, 1, DATA_LEN, fp);
    fclose(fp);

    int data_crc[4] = { 0 }; 
    int header_off = 0;
    int data_off = 0; 
    int i;                   
    int j;                  
    int k;                   
    int len;                  
    int x;                    
    int A[DIGITS] = { 0 };   
    int check = 1;          
    int flag[16] = {145, 123, 251, 160, 5, 155, 225, 184, 204, 190, 58, 168, 205, 3, 3, 211};
    
    if(buf1[0] != 'K')   my_error(); 
    if(buf1[1] != '-')   my_error(); 
    if(buf1[2] != 'P')   my_error(); 
    if(buf1[3] != 'U')   my_error(); 
    if(buf1[4] != 'B')   my_error(); 
    if(buf1[5] != '\x00')    my_error(); 
    if(buf1[6] != '\x00')    my_error(); 
    if(buf1[7] != BASE)    my_error(); 
    header_off = buf1[12]+((unsigned int)buf1[13]<<8); 
    data_off = buf1[14]+((unsigned int)buf1[15]<<8);

    for(i=0;i!=65;i++){ 
        len = buf1[i+header_off];  
        for(j=0;j!=len;j++){ 
            data_crc[k%4] ^= buf1[data_off+k]; 
            W[i][j] = buf1[data_off+k]; 
            k++; 
        } 


    } 
    
    if(data_crc[0] != buf1[8])   my_error(); 
    if(data_crc[1] != buf1[9])   my_error(); 
    if(data_crc[2] != buf1[10])  my_error(); 
    if(data_crc[3] != buf1[11])  my_error(); 

    if(buf2[0] != 'K')   my_error(); 
    if(buf2[1] != '-')   my_error(); 
    if(buf2[2] != 'P')   my_error();
    if(buf2[3] != 'R')   my_error();
    if(buf2[4] != 'I')   my_error();
    if(buf2[5] != 'V')   my_error();
    if(buf2[6] != '\01') my_error();
    if(buf2[7] != BASE)  my_error();

    memset(data_crc, 0, sizeof(data_crc));
    header_off = buf2[12]+((unsigned int)buf2[13]<<8); 
    data_off = buf2[14]+((unsigned int)buf2[15]<<8);
    k = 0;
    for(i=0;i!=64;i++){
        len = buf2[i+header_off];
        x = 1;
        for(j=0;j!=len;j++){
            data_crc[k%4] ^= buf2[data_off+k];
            key[i] += buf2[data_off+k]*x;
            x *= BASE;
            k++;
        }
    }
    if(data_crc[0] != buf2[8])   my_error();
    if(data_crc[1] != buf2[9])   my_error();
    if(data_crc[2] != buf2[10])  my_error();
    if(data_crc[3] != buf2[11])  my_error();

    for(i=0;i!=KEY_LEN;i++){
        for(j=0;j!=key[i];j++){ 
            add(A, W[i]);
        }
    } 

    for(i=0;i!=256;i++){ 
        if(A[i] != W[KEY_LEN][i]) my_error(); 
    }

    for(i=0;i<KEY_LEN;i++){ 
        flag[i%16] ^= key[i];
    } 

    printf("YOU WIN!! Here is your flag : WCTF{");
    for(i=0;i<16;i++){
        printf("%c", flag[i]);
    }
    printf("}\n");
    return 0;
}
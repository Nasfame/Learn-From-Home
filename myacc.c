#include<stdio.h>
#include <string.h> 
  

void main(){
	int n;char ch;
	char result[3]="";
	printf("How long is your jargon ##including spaces");
	scanf("%d",&n);
	char jargon[n];
	printf("Type ur jargon now");
	scanf("%s",&jargon);
	result[0] = jargon[0];
	
	for(int i=0;i<n;i++){
		if(jargon[i]==' '){
		 ch = jargon[i+1];
		
		 strncat(result,&ch,1);
		 
		
			
		}
		
		
	}
	
	
	
	
}
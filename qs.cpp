#include <bits/stdc++.h>
using namespace std;

int partition(int input[],int s,int e)
{
    int pivot=input[0];
    int pI=0;
    for(int i=1;i<=e;i++)
    {
        if(pivot>input[i]){
            pI++;
        }
    }
    
    swap(input[0],input[pI]);
    
    int i=s;
    int j=pI+1;
    while(i<pI and j<e)
    {
        if(input[i]<pivot){
            i++;
        }
        else if(input[j]>pivot){
            j++;
        }
        else{
            swap(input[i],input[j]);
        }
    }
    
    return pI;
}






void quick_sort(int input[],int s, int e)
{
    if(s>=e){
        return;
    }
    
    int pI=partition(input,s,e);
    quick_sort(input,s,pI-1);
    quick_sort(input,pI+1,e);
    
    
}



void quickSort(int input[], int size) {
    int s=0;
    int e=size-1;
    quick_sort(input,s,e);    

}

int main(){
    int n;
    cin >> n;
  
    int *input = new int[n];
    
    for(int i = 0; i < n; i++) {
        cin >> input[i];
    }
    
    quickSort(input, n);
    for(int i = 0; i < n; i++) {
        cout << input[i] << " ";
    }
    
    delete [] input;

}



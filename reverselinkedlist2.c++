#include <iostream>
using namespace std;
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* temp=head;
        left--;
        right--;
        int arr[500];
        int i=0;
        while(temp!=NULL){
            arr[i]=temp->val;
            i++;
            temp=temp->next;
        }
        int ref[i];
        temp=head;
        for(int x=0;x<i;x++){
            ref[x]=arr[x];
    
        }
        while(left!=right){
            int t=ref[left];
            ref[left]=ref[right];
            ref[right]=t;
            left++;
            right--;
        }for(int x=0;x<i;x++){;
            cout<<ref[x]<<"->";
        }
        temp=head;
        i=0;
        while(temp!=NULL){
            temp->val=ref[i];
            i++;
            temp=temp->next;
        }
        return head;
    }
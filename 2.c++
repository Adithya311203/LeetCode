/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 void insertAtTail(ListNode* &head, int val){
    ListNode* n=new ListNode(val);
    if(head==NULL){
        head=n;
        return;
    }
 
    ListNode* temp= head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=n;}
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int arr[100]={},arr2[100]={};
        int y=0;
        ListNode* temp=l1;
        while(temp!=NULL){
            arr[y]=temp->val;
            temp=temp->next;
            y++;
        }
        int y1=y;
        y=0;
        ListNode* temp2=l2;
        while(temp2!=NULL){
            arr2[y]=temp2->val;
            temp2=temp2->next;
            y++;
        } int f=0;
        int xyz[100]={};
        int ind=0,rem=0;
        for(int i=0;i<max(y,y1);i++){
            int c=arr[i]+arr2[i];
            //cout<<c<<"-";
            if(c<10){
              
                xyz[ind]+=c+rem;
              
                //cout<<"HERE>>"<<xyz[ind]<<endl;
                rem=0;
                ind++;
            }
            else{ f=1;
                xyz[ind]=c%10+rem;
                rem=0;
                cout<<"HERE>>"<<xyz[ind]<<endl;
                rem+=c/10;
                ind++;
            }

        }
        cout<<endl;
        for(int i=0;i<max(y,y1);i++){
            if(xyz[i]>9){f=1;
                xyz[i+1]+=xyz[i]/10;
                xyz[i]%=10;
            }
            
        }
        for(int i=0;i<max(y,y1)+1;i++){cout<<xyz[i]<<",";}
        return l2;
    }
};
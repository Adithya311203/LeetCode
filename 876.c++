struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void insert(ListNode* &head,int val){
    ListNode* n=new ListNode(val);
    if(head==NULL){
        head=n;
        return;
    }
    ListNode* temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=n;
    temp->next->next=NULL;
}

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int x=0;
        ListNode* temp=head;
        while(temp!=NULL){
            temp=temp->next;
            x++;
        }
        x=x/2+1;
        temp=head;
        int i=1;
        ListNode* newlist=NULL;
        while(i<x){
            temp=temp->next;
            i++;
        }
        
        while(temp!=NULL){
            cout<<"HERE:"<<temp->val<<"->";
            insert(newlist,temp->val);
            temp=temp->next;
        }
        return newlist;
    }
};
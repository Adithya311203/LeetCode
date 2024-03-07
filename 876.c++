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
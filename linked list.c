#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<ctype.h>

struct Node
{
    int data;
    struct Node* next;
}*head=NULL;
int count=0;
/*void size_list();
void insert_front(struct Node**,int);
void insert_random(struct Node*,int);
void insert_last(struct Node**,int);
void delete_node(struct Node**,int);/*/

void size_list()
{
        count++;
        if(count==1)
        {
            int l;
            printf("Enter linked list size: ");
                scanf("%d",&l);
    int i,x;
     for(i=1;i<=l;i++)
    {
        struct Node *newnode,*current;
        newnode=(struct Node*)malloc(sizeof(struct Node));
        printf("enter data: ");
        scanf("%d",&x);
        newnode->data=x;
        newnode->next=NULL;
        if(head==NULL)
        {
            head=newnode;
            current=newnode;
        }
        else
        {
            current->next=newnode;
            current=newnode;
        }
    }
        }
        else
            printf("No more changes Refer to statement 1\n\n");
    }
void insert_front(struct Node** head_ref,int new_data)
{
    struct Node* new_node;
    new_node=(struct Node*)malloc(sizeof(struct Node));
    new_node->data=new_data;
    new_node->next=*head_ref;
    *head_ref=new_node;
    printf("\n\n");
}

void insert_random(struct Node* prev_node,int new_data)
{
    if(prev_node==NULL)
    {
        printf("Previous Node should not be NULL\n\n");
        return;
    }
    struct Node* newnode;
    newnode=(struct Node*)malloc(sizeof(struct Node));
    newnode->data=new_data;
    newnode->next=prev_node->next;
    prev_node->next=newnode;
}

void insert_last(struct Node** head_ref,int new_data)
{
    struct Node* newnode;
    struct Node* last=*head_ref;
    newnode=(struct Node*)malloc(sizeof(struct Node));
    newnode->data=new_data;
    newnode->next=NULL;
    if(*head_ref==NULL)
    {
        *head_ref=newnode;
        return;
    }
    while(last->next!=NULL)
    {
        last=last->next;
    }
    last->next=newnode;
    return;
}

void delete_node(struct Node** head_ref,int key)
{
    struct Node* temp=*head_ref;
    struct Node* prev;
    if(temp!=NULL&&temp->data==key)
    {
        *head_ref=temp->next;
        free(temp);
        return;
    }
    while(temp!=NULL&&temp->data!=key)
    {
        prev=temp;
        temp=temp->next;
    }
    if(temp==NULL)return;
    prev->next=temp->next;
    free(temp);
}

void main()
{
    int n,l,ele,key;
    while(1>0)
    {
        printf("1. Enter size of linked list(You are allowed to perform this operation only once)\n");
        printf("2. Insertion of new element at front\n");
        printf("3. Insertion of new element at random\n");
        printf("4. Insertion of new element at last\n");
        printf("5. Deletion of element\n");
        printf("6. exit\n\n");
        printf("Enter Your Choice: ");
        scanf("%d",&n);
        switch(n)
        {
        case 1:
            {
                size_list();
                break;
            }
        case 2:
            {
                printf("Enter the element to be inserted: ");
                scanf("%d",&ele);
                insert_front(&head,ele);
                printf("\n");
                break;
            }
        case 3:
            {
                printf("Enter the element after which you want to insert a new Element: ");
                scanf("%d",&key);
                printf("Enter the element to be inserted: ");
                scanf("%d",&ele);
                struct Node* temp=head;
                while(temp!=NULL&&temp->data!=key)
                    {
                       temp=temp->next;
                    }
                insert_random(temp,ele);
                printf("\n");
                break;
            }
        case 4:
            {

                printf("Enter the element to be inserted: ");
                scanf("%d",&ele);
                insert_last(&head,ele);
                printf("\n");
                break;
            }
        case 5:
            {
                printf("Enter the element to be deleted: ");
                scanf("%d",&ele);
                delete_node(&head,ele);
                printf("\n");
                break;
            }
        case 6:
            {
                exit(0);
                break;
            }
        default:
            {
                printf("Enter a valid choice\n\n");
                break;
            }


        }
    struct Node* temp=head;
    printf("\nYour linklist is as follows: ");
    while(temp!=NULL)
    {
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL\n\n");
    if(isalpha(n)!=0)
    {
        break;
    }
    }

}

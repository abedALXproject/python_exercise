#include <stdio.h>
#include <stdlib.h>
#define MAX 5
void insert();
void delete();
void display();
int queue_array[MAX];
int rear = -1;
int front = - 1;


int main()
{
	int choice;
	while(1)
	{
		printf("1. Insert element to queue \n");
		printf("2. Delete element from queue \n");
		printf("3. Display all elements of queue \n");
		printf("4. Quit \n");
		printf("Enter your choice: ");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				insert();
				break;
			case 2:
				delete();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(1);
			default:
				printf("Wrong choice \n");
		}
	}
}

void insert(int item)
{
	if((front == 0 && rear == MAX-1) || (front == rear+1))
	{
		printf("Queue Overflow n");
		return;
	}
	if(front == -1)
	{
		front = 0;
		rear = 0;
	}
	else
	{
		if(rear == MAX-1)
			rear = 0;
		else
			rear = rear+1;
	}
	cqueue_arr[rear] = item ;
}

void deletion()
{
	if(front == -1)
	{
		printf("Queue Underflown");
		return ;
	}
	printf("Element deleted from queue is : %dn",cqueue_arr[front]);
	if(front == rear)
	{
		front = -1;
		rear=-1;
	}
	else
	{
		if(front == MAX-1)
			front = 0;
		else
			front = front+1;
	}
}


void display()
{
	int front_pos = front,rear_pos = rear;
	if(front == -1)
	{
		printf("Queue is emptyn");
		return;
	}
	printf("Queue elements :n");
	if( front_pos <= rear_pos )
		while(front_pos <= rear_pos)
		{
			printf("%d ",cqueue_arr[front_pos]);
			front_pos++;
		}
	else
	{
		while(front_pos <= MAX-1)
		{
			printf("%d ",cqueue_arr[front_pos])
				front_pos++;
		}
		front_pos = 0;
		while(front_pos <= rear_pos)
		{
			printf("%d ",cqueue_arr[front_pos]);
			front_pos++;
		}
	}
	printf("n");
}
int main()
{
	int choice,item;
	do
	{
		printf("1.Insertn");
		printf("2.Deleten");
		printf("3.Displayn");
		printf("4.Quitn");
		printf("Enter your choice : ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1 :
				printf("Input the element for insertion in queue : ");
				scanf("%d", &item);
				insert(item);
				break;
			case 2 :
				deletion();
				break;
			case 3:
				display();
				break;
			case 4:
				break;
			default:
				printf("Wrong choicen");
		}
	}while(choice!=4);
	return 0;
}

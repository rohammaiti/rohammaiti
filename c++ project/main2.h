
#include<iostream>
using namespace std;
#define size 100
class airlines
{
public:
	airlines();
	void main_menu();
	void MAKERESEVATION();
	void CANCELRESERVATION();
	void SEARCHPASSENGER();
	void CHANGERESERVATION();
	void PRINTLIST();
	void REPORT();
private:
	struct node
	{
		string firstname, lastname, ID, phone_num, menu;
		int reserve_num, seat_num;
		node *next;
	};
	node *start;
	node *temp, *temp2;
}PLANE;
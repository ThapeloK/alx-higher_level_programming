#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop
 * @list: linked list
 * Return: 1 if it has a loop, 0 if there is no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;

	if (!list)
		return (0);
	while (list && fast && fast->next)
	{
		fast = fast->next->next;
		list = list->next;
		if (list == fast)
			return (1);
	}
	return (0);
}

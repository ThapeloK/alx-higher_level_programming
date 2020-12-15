#include "lists.h"

/**
 * reverse - reverses linked list
 * @h: Linked list
 * Return: reversed list
 */
listint_t *reverse(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*h)
	{
		next = (*h)->next;
		(*h)->next = prev;
		prev = *h;
		*h = next;
	}
	*h = prev;
	return (*h);
}

/**
 * is_palindrome - reverses linked list
 * @h: Linked list
 * Return: reversed list
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = NULL;

	if (!*head)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;
	fast = *head;
	temp = reverse(&slow);
	while (slow)
	{
		if (fast->n != slow->n)
		{
			reverse(&temp);
			return (0);
		}
		fast = fast->next;
		slow = slow->next;
	}
	reverse(&temp);
	return (1);
}

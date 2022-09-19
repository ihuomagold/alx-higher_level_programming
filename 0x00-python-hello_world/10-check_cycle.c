#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 * 
 */

int check_cycle(listint_t *list)
{
	listint_t *l1 = list;
	listint_t *l2 = list;

	if (!list)
		return (0);

	while (l1 && l2 && l2->next)
	{
		l1 = l1->next;
		l2 = l2->next->next;
		if (l1 == l2)
			return (1);
	}
	return (0);
}

#include "lists.h"

/**
 *check_cycle - checks if a list has a cycle
 *@list: linked list to check
 *Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *camel = list;
	listint_t *horse = list;

	if (!list)
		return (0);
	while (camel && horse->next)
	{
		if (camel == horse)
			return (1);
		camel = camel->next;
		horse = horse->next->next;
	}
	return (0);
}

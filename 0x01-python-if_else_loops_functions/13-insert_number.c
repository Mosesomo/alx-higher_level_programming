#include "lists.h"

/**
 *insert_node - insert a number in a singly list
 *@head: pointer to the list
 *@number: value to insert
 *Return: Null if failed or address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *node = *head;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;

	if (!node && node->n >=number)
	{
		newnode->next = node;
		(*head) = newnode;
		return (newnode);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	newnode->next = node->next;
	node->next = newnode;
	return (newnode);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: adpusel <adpusel@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/10/19 10:48:07 by adpusel           #+#    #+#             */
/*   Updated: 2017/11/16 12:45:50 by adpusel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <libft.h>
#include <stdbool.h>

typedef enum
{
	INTEGER,
	PLUS,
	MINUS,
	DIV,
	MUL
} e_type;

typedef struct s_token
{
	e_type type;
	int value;
} t_token;

char *del_space(char *str)
{
	while (*str == ' ')
		str++;
	return (str);
}

void lexer(char *str, t_array *array)
{
	t_token t;
	int pos;
	static char *sign = "+-/*";
	static e_type type[4] = { PLUS, MINUS, DIV, MUL };

	while (*str)
	{
		ft_bzero(&t, sizeof(t_token));
		str = del_space(str);
		if (ft_isdigit(*str))
		{
			t.type = INTEGER;
			t.value = ft_atoi(str);
		}
		else if (-1 != (pos = ft_strchr_int(sign, *str)))
		{
			t.type = type[pos];
			t.value = *str;
		}
		else
		{
			printf("error lexer, bad asking");
			return;
		}
		ftarray__push(array, &t);
		str += 1;
	}
}



int print_token(void *p_el, void *param)
{
	t_token *t;

	(void)param;
	t = p_el;
	if (t->type == INTEGER)
		ft_printf("%d", t->value);
	else
		ft_printf(" %c ", t->value);
	return (0);
}

// if the token has the right type, I add 1 to the current, and ret true
int eat(t_array *array, e_type type)
{
	t_token *t;

	t = ftarray__current(array);
	if (t->type == type)
	{
		array->i += 1;
		return (t->value);
	}
	ft_printf("error syntax analyze");
	exit(-42);
}

int factor(t_array *array)
{
	return (eat(array, INTEGER));
}

int term(t_array *a)
{
	t_token *t;
	int nb;
	int result;

	result = factor(a);
	while (NULL != (t = ftarray__current(a))
		   && (t->type == MUL || t->type == DIV))
	{
		if (t->type == MUL)
		{
			eat(a, MUL);
			nb = factor(a);
			result = result * nb;
		}
		if (t->type == DIV)
		{
			eat(a, DIV);
			nb = factor(a);
			result = result / nb;
		}
	}
	return (result);
}

int expr(t_array *a)
{
	t_token *t;
	int result;

	result = term(a);
	while (NULL != (t = ftarray__current(a))
		   && (t->type == PLUS || t->type == MINUS))
	{
		if (t->type == PLUS)
		{
			eat(a, PLUS);
			result = result + term(a);
		}
		if (t->type == MINUS)
		{
			eat(a, MINUS);
			result = result - term(a);
		}
	}
	return (result);
}

int main(int ac, char **av)
{
	(void)ac;
	t_array *array = ftarray__init(20, sizeof(t_token));

	lexer(av[1], array);
	ftarray__func(array, print_token, NULL);
	ft_printf("\n");
	array->i = 0;
	ft_printf("%d\n", expr(array));
	return (0);
}
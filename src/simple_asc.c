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

void calcule(t_array *array)
{
	t_token *nb;
	t_token *sign;

	int result = ((t_token *)ftarray__at(array, 0))->value;
	array->i = 1;

	while (NULL != (sign = ftarray__next(array)))
	{
		if (sign->type == INTEGER)
		{
			ft_printf("syntax error");
			return;
		}
		nb = ftarray__next(array);
		if (!sign || !nb || nb->type != INTEGER)
		{
			ft_printf("check error");
			return;
		}
		if (sign->type == MINUS)
			result -= nb->value;
		if (sign->type == PLUS)
			result += nb->value;
	}
	ft_printf("%d", result);
}

int main(int ac, char **av)
{
	(void)ac;
	t_array *array = ftarray__init(20, sizeof(t_token));

	lexer(av[1], array);
	ftarray__func(array, print_token, NULL);
	ft_printf("\n");
	calcule(array);
	return (0);
}
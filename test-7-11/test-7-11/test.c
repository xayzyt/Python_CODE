#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//int my_strlen(char* str)
//{
//	int count = 0;
//	while (*str != '\0')
//	{
//		count++;
//		str++;
//	}
//	return count;
//}

//�ݹ����
//int my_strlen(char* str)
//{
//	if (*str != '\0')
//	{
//		return 1 + my_strlen(str + 1);
//	}
//	else
//		{
//		return 0;
//	}
//}
//int main() {
//	//��д��������������ʱ���������ַ������ȡ�
//	char arr[] = "abc";
//	int len = my_strlen(arr);
//	printf("%d\n", len);
//	return 0;
//}


//��n�Ľ׳�
//�ݹ�ʵ��
//int fac(int n)
//{
//	if (n<=1)
//	{
//		return 1;
//	}
//	else
//	{
//		return n * fac(n - 1);
//	}
//}
//int main()
//{
//	int n = 0;
//	scanf("%d", &n);
//	int ret = fac(n);
//	printf("%d\n", ret);
//	return 0;
//}

//��쳲��������еĵ�n��
//쳲��������еĶ��壺f(0)=0,f(1)=1,f(n)=f(n-1)+f(n-2)(n>=2)
// �ݹ�ʵ��
//int Fib(int n)
//{
//	if(n<=2)
//		return 1;
//	else
//		return Fib(n - 1) + Fib(n - 2);
//}
// ����ʵ��
//int Fib(int n)
//{
//	if (n <= 2)
//		return 1;
//	int a = 1, b = 1, c = 0;
//	for (int i = 3; i <= n; i++)
//	{
//		c = a + b;
//		a = b;
//		b = c;
//	}
//	return c;
//}
//
//int main()
//{
//	int n = 0;
//	scanf("%d", &n);
//	int ret = Fib(n);
//	printf("%d\n", ret);
//	return 0;
//}


//д���뽫���������Ӵ�С���
//int main()
//{
//	int a = 0, b = 0, c = 0;
//	scanf("%d %d %d", &a, &b, &c);
//	if (a < b)
//	{
//		int tmp = a;
//		a = b;
//		b = tmp;
//	}
//	if (a < c)
//	{
//		int tmp = a;
//		a = c;
//		c = tmp;
//	}
//	if (b < c)
//	{
//		int tmp = b;
//		b = c;
//		c = tmp;
//	}
//	printf("%d %d %d\n", a, b, c);
//	return 0;
//}


//��ӡ1-100֮������3�ı���������
//int main()
//{
//	int i = 1;
//	for (i = 1; i <= 100; i++)
//	{
//		if (i % 3 == 0)
//		{
//			printf("%d ", i);
//		}
//	}
//	return 0;
//}

//�����������������Լ��
//int main()
//{
//	int a = 0;
//	int b = 0;
//	int small = 0;
//	scanf("%d %d", &a ,& b);
//	if (a < b)
//	{
//		small = a;
//	}
//	else
//	{
//		small = b;
//	}
//	int i = 0;
//	int gcd = 0; // ���Լ����ʼֵΪ0
//	for (i = 1; i <= small; i++)
//	{
//		if (a % i == 0 && b % i == 0)
//		{
//			gcd = i;
//		}
//	}
//	printf("%d", gcd);
//	
//	return 0;
//}
//շת����������Լ��
//int main()
//{
//	int a = 0;
//	int b = 0;
//	int c = 0;
//	scanf("%d %d", &a, &b);
//	while (c=a%b)
//	{
//		a = b;     // ��b��ֵ��a
//		b = c;     // ��������ֵ��b
//	}
//	printf("%d\n", b); // ������Լ��
//	return 0;
//}

//��1-100�ж��ٸ�9
//int main()
//{
//	int count = 0;
//	int i = 0;
//	for (i = 1; i <= 100; i++) {
//	//���λ��
//		if (i % 10 == 9) {
//			count++;
//		}	
//	//��ʮλ��
//		if (i / 10 == 9) {
//			count++;
//		}	
//	}
//	printf("%d", count);
//	return 0;
//}


//��ʮ���������ֵ

//int main()
//{
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	int max = arr[0];
//	int i = 0;
//		for (i = 1; i < 10; i++)
//		{
//			if (arr[i] > arr[0])
//			{
//				max = arr[i];
//			}
//		}
//	printf("%d", max);
//	return 0;
//}

//����Ļ��ӡ9*9�˷���
//int main()
//{
//	int i = 0;
//	for (i = 1; i <= 9; i++)
//	{
//		int j = 0;
//		for (j = 1; j <= i; j++) {
//
//			printf("% d * %d = % -2d \t ", i, j, i * j);
//		}
//		printf("\n");
//	}
//	return 0;
//}


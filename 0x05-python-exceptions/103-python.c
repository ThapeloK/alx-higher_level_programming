#include <Python.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte;
	unsigned int i;
	unsigned long size;
	char *string;

	printf("[.] bytes object info\n");
	if (p == NULL || p->ob_type != &PyBytes_Type)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	byte = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %lu\n", size);
	string = byte->ob_sval;
	printf("  trying string: %s\n", string);
	if (size >= 10)
		size = 10;
	else
		size++;
	printf("  first %lu bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", string[i] & 0xff);
		if (i + 1 < size)
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	PyFloatObject *l;
	char *buf;
	unsigned int strlng, i;

	buf = malloc(1000);
	printf("[.] float object info\n");
	if (p == NULL || p->ob_type != &PyFloat_Type)
	{
		printf("  [ERROR] Invalid Float Object\n");
		free(buf);
		return;
	}
	l = (PyFloatObject *) p;
	if (abs(l->ob_fval) >= 1)
		sprintf(buf, "%.16G", l->ob_fval);
	else if (l->ob_fval == 0 || l->ob_fval == -0)
		sprintf(buf, "%.16G", l->ob_fval);
	else
	{
		sprintf(buf, "%.16lf", l->ob_fval);
		for (i = 2; i < strlen(buf); i++)
		{
			if (buf[0] == '-')
				i++;
			if (buf[i] != '0')
			{
				buf[i + 1] = '\0';
				break;
			}
		}
	}
	if (strpbrk(".", buf) == NULL)
	{
		strlng = strlen(buf);
		buf[strlng] = '.';
		buf[strlng + 1] = '0';
		buf[strlng + 2] = '\0';
	}
	printf("  value: %s\n", buf);
	free(buf);
}

void print_python_list(PyObject *p)
{
	PyTypeObject *type;
	PyObject *item;
	PyListObject *list;
	unsigned long size;
	unsigned int i;

	printf("[*] Python list info\n");
	if (p != NULL && p->ob_type == &PyList_Type)
	{
		list = (PyListObject *)p;
		size = ((PyVarObject *)p)->ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			item = list->ob_item[i];
			type = item->ob_type;
			printf("Element %d: %s\n", i, type->tp_name);
			if (item->ob_type == &PyBytes_Type)
				print_python_bytes(item);
			else if (item->ob_type == &PyFloat_Type)
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

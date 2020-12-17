#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <stdlib.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Print python list info
 * @p: PyObject
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	/* PyBytesObject *obj = (PyBytesObject *)p; */
	char *str = NULL;
	int size = 0, i = 0, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)p)->ob_sval;
	size = PyBytes_Size(p);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	max  = size + 1;
	if (max > 10)
		max = 10;
	printf("  first %i bytes: ", max);
	for (i = 0; i < max; i++)
	{
		if (i != max - 1)
			printf("%02hhx ", str[i]);
		else
			printf("%02hhx\n", str[i]);
	}
}

/**
 * print_python_list_info - Print python list info
 * @p: PyObject
 * Return: Nothing
 */
		void print_python_list(PyObject *p)
		{
			ssize_t a = 0;
			PyListObject *obj = (PyListObject *)p;

			printf("[*] Python list info\n");
			printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
			printf("[*] Allocated = %ld\n", obj->allocated);
			for (; a < PyList_Size(p); a++)
			{
				printf("Element %ld: %s\n", a, (obj->ob_item[a])->ob_type->tp_name);
				if (strcmp((obj->ob_item[a])->ob_type->tp_name, "bytes") == 0)
					print_python_bytes(obj->ob_item[a]);
			}
		}

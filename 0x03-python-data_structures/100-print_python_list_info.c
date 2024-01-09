#include <python.h>
#include <object.h>
#include "listobject.h"
void print_python_list_info(PyObject *p);
{
	long int size = pyList_size(p);
	int i;
	pyListobject *obj = (pyListobject *)p;

	printf("[*] Size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; 1 < size; i++)
		print("element %i: %li\n", i, py_TYPE(obj->ob_item[i])->tp_name);
}

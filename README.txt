Esta aplicación consiste en el desarrollo de un inventario de una pequeña tienda en la cual se puede registrar, actualizar, eliminar y mostrar los productos
que se encuentren en la misma. Se puede realizar busquedas de un producto que haya sido registrado en la misma, como también la generación de un reporte
que indica el limite de stock de un producto.

Los productos de la tienda son registrados en una base de datos llamada "Inventario".

A continuación, comenzaré a desarrollar las siguientes funcionalidades:
	- Registro de productos: El usuario podrá agregar nuevos productos al inventario, solicitandole los siguientes datos: nombre, descripción, 
	  cantidad, precio y categoría.
	- Visualización de productos: La aplicación muestra todos los productos registrados en el inventario, incluyendo su ID, nombre, descripción, cantidad, precio 
	  y categoría.
	- Actualización de productos: El usuario podrá actualizar la cantidad disponible de un producto específico utilizando su ID.
	- Eliminación de productos: El usuario podrá eliminar un producto del inventario utilizando su ID.
	- Búsqueda de productos: El usuario podrá buscar productos por su ID, mostrando los resultados que coincidan con los criterios de su búsqueda. 
	  De manera opcional, podrá buscar por nombre o categoría.
	- Reporte de Bajo Stock: El usuario podrá generar un reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario.
#include<linux/init.h>
#include<linux/module.h>

int simple_module_init(void){

	printk(KERN_INFO"HELLO WORLD %s",__FUNCTION__);
	return 1;

}
void simple_module_exit(void){

	printk(KERN_INFO"BYE WORLD %s",__FUNCTION__);

}
module_init(simple_module_init);
module_exit(simple_module_exit);


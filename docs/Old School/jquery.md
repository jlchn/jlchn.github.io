
## Operating Select Component

### get text and value of selected option

``` javascript

var checkText=$("#select_id").find("option:selected").text();
var checkValue=$("#select_id").val();
var checkIndex=$("#select_id ").get(0).selectedIndex;

```

###  add and remove options

```javascript
$("#select_id").append("<option value='Value'>Text</option>"); 
$("#select_id").prepend("<option value='0'>Please Select</option>");
$("#select_id option:last").remove(); 
$("#select_id option[index='0']").remove(); 
$("#select_id option[value='3']").remove(); 
$("#select_id option[text='4']").remove();
 ```

 ### clear all options

 ```javascript

$("#select_id").empty();
 ```
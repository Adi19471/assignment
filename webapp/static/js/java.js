// this form filed assigning area ...
var options = document.getElementById('selected-area').selectedOptions;
var values = Array.from(options).map(({ value }) => value);
console.log(values);


// selected multiple


document.getElementById('call_to_people').onclick = function() {
    var selected = [];
    for (var option of document.getElementById('pets').options)
    {
        if (option.selected) {
            selected.push(option.value);
        }
    }
    alert(selected);
}

// scroll down 

function id_call_to_people() {
    document.getElementById('id_call_to_people').scrollTop =  document.getElementById('id_call_to_people').scrollHeight
   }
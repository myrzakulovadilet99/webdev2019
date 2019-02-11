
var newTask = function(e)

{
    var myList = document.getElementById('List');


    var myInput = document.getElementById('Input');

var myClicker = document.getElementById('btn');


    if(myInput.value !== "")

    {

        var newLi = document.createElement('li');


        var newCheck = document.createElement('input');

        var newSpan = document.createElement('span');

        var newImg = document.createElement('img');

        var newP = document.createElement('p');

        newImg.className = "myImage";

        newImg.src = "delete.jpg";

        newCheck.type = "checkbox";

        newCheck.className = "Check";

        newSpan.className = "Span";


        newP.innerHTML = myInput.value;

        newCheck.onclick = onLiClick;

        newImg.onclick = deletAll;

        newSpan.appendChild(newCheck);


        newSpan.appendChild(newP);

        newLi.appendChild(newSpan);

        newLi.appendChild(newImg);

        myList.appendChild(newLi);

        myInput.value = "";

        

    }

    else{

        alert("Input is UNDEFINED!!!");

    }

};



var onLiClick = function(e)

{

    // var i  = 1;

    if(e.target.checked)

    {

        var cur = e.target.parentNode;

        cur.className = "newDivClass";

    }

    else{

        var cur = e.target.parentNode;

        cur.className = "Span";

    }

    console.log(e.target);

   

};

 

var deletAll  = function(e)

{

    var bigLi = event.target.parentNode;

    bigLi.remove();

}
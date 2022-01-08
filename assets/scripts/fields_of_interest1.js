var click_state = new Array (false, false,false,false,false,false,false,false);
var button_id = new Array ("cs", "ds", "ph", "bio", "ch", "mt", "eg", "ud");
counter = 0;

function selected(id){
	var index = button_id.indexOf(id);
	if (counter<3 && click_state[index]==false){
		document.getElementById(id).style.backgroundColor = "#757BC8";
		document.getElementById(id).style.color = "white";
		click_state[index]=true;
		h_id = id + "_h";
		document.getElementById(h_id).style.color = "white";
		counter ++;
	}

	else if(click_state[index]==true){
		document.getElementById(id).style.backgroundColor = "white";
		document.getElementById(id).style.color = "black";
		click_state[index]=false;
		h_id = id + "_h";
		document.getElementById(h_id).style.color = "#757BC8";
		counter --;
	}

}

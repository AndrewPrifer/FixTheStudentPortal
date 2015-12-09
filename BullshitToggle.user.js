// ==UserScript==
// @name Student Portal Bullshit Toggle
// @author Andrew Prifer
// @description Lets you toggle the useless fixed boxes in the top row of the student portal. After installing, you will see a new button in the menu bar.
// @version 1.0
// @run-at document-end
// @match https://nestor.rug.nl/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_700_1
// ==/UserScript==

function insertAfter(newNode, referenceNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function setDisplay(option){
  var bullshit = new Array();
  // Comment out to keep the "Courses" module
  bullshit.push(document.getElementById('module:_4939_1'));
  // Comment out to keep the "Nice to know" module
  bullshit.push(document.getElementById('module:_4959_1'));
  // Comment out to keep the "Need to know" module
  bullshit.push(document.getElementById('module:_4960_1'));

  for (var i = bullshit.length - 1; i >= 0; i--) {
    bullshit[i].style.display = option;
  }
}

function handler(){
  if(document.getElementById('module:_4939_1').style.display == 'none'){
    setDisplay('block');
    this.firstChild.innerHTML = 'Bullshit On';
  } else {
    setDisplay('none');
    this.firstChild.innerHTML = 'Bullshit Off';
  }
}

var lastItem = document.getElementById('Career');

var toggle = document.createElement('td');
toggle.innerHTML = '<a>Bullshit Off</a>'

setTimeout(function() {
  setDisplay('none');
  insertAfter(toggle, lastItem);
}, 500);

toggle.addEventListener('click', handler);
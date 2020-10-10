
function submitMove() {
    var source = document.getElementById("source").value;
    var dest = document.getElementById("destination").value;
    movePiece(source, dest);
}

function movePiece(var_src, var_dest) {
    var from = document.getElementById(String(var_src).toLowerCase());
    var to = document.getElementById(String(var_dest).toLowerCase());
    to.innerHTML = from.innerHTML;
    from.innerHTML = '&nbsp;'
}
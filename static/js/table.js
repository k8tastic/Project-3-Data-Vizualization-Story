var table_data = $.getJSON('/table_data', function( data) {

  console.log(table_data);
});

  $(document).ready( function () {

     $.getJSON('/table_data', function(jsondata) {

       var data = jsondata.map(
            cols=>Object.values(cols)
          );

      $('#foreclosuretable').DataTable( {
          data: data,

          searchPane: {
                  container: '.searchPanes',
                  threshold: 0
              },
      } );

  } );
})

/*
$(document).ready( function () {
    d3.json("/foreclosure_data").then((data)=>{
    console.log({data});
        var region_name =data.map(d=>d['region_name']);
        var zstreet_address = data.map(d=>d['zstreet_address']);
        var zcity = data.map(d=>d['zcity']);
        var zstate = data.map(d=>d['zstate']);
        var zzip = data.map(d=>d['zzip']);
        var table = d3.select("tbody")

        console.log(region_name)
        for (i=0;i<region_name.length;i++){
           var tr = table.append('tr')
            tr.append('td').text(region_name[i])
            tr.append('td').text(zstreet_address[i])
            tr.append('td').text(zcity[i])
            tr.append('td').text(zstate[i])
            tr.append('td').text(zzip[i])

        }

        $('#myTable').DataTable();

    })

    });

*/
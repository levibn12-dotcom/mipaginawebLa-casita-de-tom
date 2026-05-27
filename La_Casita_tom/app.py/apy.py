from flask import Flask, render_template_string



app = Flask(__name__)



pagina_html = """

<!DOCTYPE html>

<html lang="es">

<head>

  <meta charset="UTF-8">

  <title>La Casita de Tom</title>



  <!-- Bootstrap -->

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">



  <style>



    body{

      background-color:#f8f9fa;

    }



    .navbar{

      background:#198754;

    }



    .navbar-brand{

      color:white !important;

      font-weight:bold;

      font-size:28px;

    }



    .banner{

      background-image:url("https://images.unsplash.com/photo-1521587760476-6c12a4b040da?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");

      background-size:cover;

      background-position:center;

      height:420px;

      display:flex;

      align-items:center;

      justify-content:center;

      color:white;

      text-align:center;

    }



    .banner-box{

      background:rgba(0,0,0,0.45);

      padding:30px;

      border-radius:12px;

    }



    .card img{

      height:220px;

      object-fit:cover;

    }



    footer{

      background:#198754;

      color:white;

      text-align:center;

      padding:20px;

      margin-top:40px;

    }



  </style>

</head>



<body>



<!-- Barra superior -->

<nav class="navbar navbar-expand-lg">

  <div class="container">



    <a class="navbar-brand" href="#">

      📚 La Casita de Tom

    </a>



    <form class="d-flex">

      <input class="form-control me-2" type="search" placeholder="Buscar útiles escolares">

      <button class="btn btn-light">Buscar</button>

    </form>



  </div>

</nav>



<!-- Banner -->

<section class="banner">



  <div class="banner-box">



    <h1>Todo para el regreso a clases</h1>



    <p>

      Cuadernos, mochilas, colores y mucho más

    </p>



    <button class="btn btn-success btn-lg">

      Ver promociones

    </button>



  </div>



</section>



<!-- Promociones -->

<div class="container mt-5">



  <h2 class="mb-4">

    Promociones destacadas

  </h2>



  <div class="row">



    <div class="col-md-4">



      <div class="card shadow">



        <img src="https://img.kwcdn.com/product/fancy/97a2375f-b980-4aea-8c41-6595a1eb785c.jpg?imageView2/2/w/800/q/70/format/avif">



        <div class="card-body">



          <h5>Cuadernos escolares</h5>



          <p>Pack x3 a S/ 12.00</p>



          <button class="btn btn-success">

            Ver oferta

          </button>



        </div>

      </div>

    </div>



    <div class="col-md-4">



      <div class="card shadow">



        <img src="https://thumbs.dreamstime.com/b/dos-ni%C3%B1os-con-mochila-o-bolsita-escolares-de-camino-la-escuela-sanos-y-sonrientes-hermanos-mejores-amigos-al-aire-libre-en-242873509.jpg?w=992">



        <div class="card-body">



          <h5>Mochilas</h5>



          <p>Desde S/ 45.00</p>



          <button class="btn btn-success">

            Ver oferta

          </button>



        </div>

      </div>

    </div>



    <div class="col-md-4">



      <div class="card shadow">



        <img src="https://nutesablog.wpcomstaging.com/wp-content/uploads/2024/01/tipos-de-plumones-1.jpg">



        <div class="card-body">



          <h5>Colores y plumones</h5>



          <p>Desde S/ 8.00</p>



          <button class="btn btn-success">

            Ver oferta

          </button>



        </div>

      </div>

    </div>



  </div>



</div>



<!-- Tabla -->

<div class="container mt-5">



  <h2 class="mb-4">

    Productos disponibles

  </h2>



  <table class="table table-striped table-bordered shadow">



    <thead class="table-success">



      <tr>

        <th>Producto</th>

        <th>Precio</th>

        <th>Stock</th>

      </tr>



    </thead>



    <tbody>



      <tr>

        <td>Cuaderno A4</td>

        <td>S/ 5.00</td>

        <td>50</td>

      </tr>



      <tr>

        <td>Lápiz</td>

        <td>S/ 1.00</td>

        <td>100</td>

      </tr>



      <tr>

        <td>Mochila escolar</td>

        <td>S/ 45.00</td>

        <td>15</td>

      </tr>



      <tr>

        <td>Colores x12</td>

        <td>S/ 8.00</td>

        <td>40</td>

      </tr>



      <tr>

        <td>Cartulina</td>

        <td>S/ 2.00</td>

        <td>60</td>

      </tr>



    </tbody>



  </table>



</div>



<!-- Contacto -->

<div class="container mt-5 mb-5">



  <h2>Contacto</h2>



  <p>📍 Lima - Perú - SJL(Canto Grande)</p>



  <p>📞 999 999 999</p>



  <p>🕒 Lunes a viernes: 8:00 am - 6:00 pm</p>



  <p>🕒 Sábados: 8:00 am - 1:00 pm</p>



</div>



<footer>



  © 2026 La Casita de Tom - Siempre cerca de los estudiante



</footer>



</body>

</html>

"""



@app.route("/")

def inicio():

  return render_template_string(pagina_html)



if __name__ == "__main__":

  app.run(host="0.0.0.0", port=8080)

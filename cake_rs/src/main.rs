use actix_web::{get, web, App, HttpServer, Responder};


#[get("/cakes/welcome/")]
async fn index(_name: web::Path<String>) -> impl Responder {
    format!("working here!")
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
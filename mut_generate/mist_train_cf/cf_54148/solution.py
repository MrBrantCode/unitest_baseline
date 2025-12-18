"""
QUESTION:
Create a function named `configure_traefik_wordpress` that configures Traefik to deploy WordPress on a specified domain. The function should take two parameters: `domain_name` and `port`. The function should return the required configuration in a format similar to a Docker Compose file. The domain should be routed to the WordPress service, and Traefik's entrypoints should be configured to listen on ports 80 and 443.
"""

def configure_traefik_wordpress(domain_name, port):
    return f"""
version: '3'

services:
  wordpress:
    image: wordpress
    ports:
      - {port}
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.wordpress.rule=Host(`{domain_name}`)"
      - "traefik.http.routers.wordpress.entrypoints=web"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress:/var/www/html

  db:
    image: mysql:5.7
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
      MYSQL_ROOT_PASSWORD: wordpress
    volumes:
      - db:/var/lib/mysql

volumes:
  wordpress:
  db:

networks:
  default:
    external:
      name: web
"""
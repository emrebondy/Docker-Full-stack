FROM httpd:2.4

COPY ./src /usr/local/apache2/htdocs/
COPY ./myapp.conf /usr/local/apache2/conf/extra/myapp.conf

RUN sed -i '/LoadModule proxy_module/s/^#//g' /usr/local/apache2/conf/httpd.conf \
    && sed -i '/LoadModule proxy_http_module/s/^#//g' /usr/local/apache2/conf/httpd.conf

RUN echo "Include conf/extra/myapp.conf" >> /usr/local/apache2/conf/httpd.conf

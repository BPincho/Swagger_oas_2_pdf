# Swagger_oas_2_pdf
Modular application that can be used to directly convert a json swagger oas to a static pdf file.

<h2> But why? </h2>
<p> Had to convert a swagger oas to pdf in a transparent manner. Found many partial solutions online, but none fully integrated everything, so i sort off created one and made it public for the good people of the internet. </p>
<p> This app uses Swagger2markup-cli to convert swagger oas to markup and asciidoctor-pdf to convert from markup to pdf with some python to glue everything together nicely. Therefore i used:</p>
<ul>
  <li> Java 8 </li>
  <li> Ruby with some pretty gems(listed in the gemfile) </li>
  <li> Python3 </li>
</ul>

<p> Usage is simple, build the image run the container and call the endpoint with a valid url, your browser should then prompt a file download.</p>

Example:

```bash
lvh.me:5000/https://petstore.swagger.io/v2/swagger.json
```

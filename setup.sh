mkdir -p ~/.streanlit/
echo "\
[general]\n\
email = \"joaopedromonteiro2014@gmail.com\"\n\
"> ~/.streamlit/credentials.toml

echo"\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/contfig/toml
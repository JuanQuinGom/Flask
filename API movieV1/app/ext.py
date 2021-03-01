#instanciar extensiones a usar en la aplicacion
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

## Instanciar las distintas extensiones que utilicemos en la aplicación
ma = Marshmallow()
migrate = Migrate()
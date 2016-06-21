#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
#   jorgescalona@riseup.net   @jorgemustaine  https://github.com/jorgescalona
#
##############################################################################
from openerp import api, fields, models
import inspect, os

class res_company(models.Model):
    """clase heredada de res_company"""
    _name = 'res.company'
    _inherit = ['res.company']

    # Herencia a un metodo
    def _get_logo(self, cr, uid, ids):
    	# obtenemos el path actual
    	ruta_actual=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    	ruta_actual=ruta_actual.split('models')
    	ruta_actual=''.join(ruta_actual)
    	return open(os.path.join(
    								ruta_actual,
    								'static',
    								'img',
    								'res_company_logo.png'
    							), 'rb') .read().encode('base64')


    rif = fields.Char('Rif', size=15, required=True, help='Aqui  se agrega el rif de la universidad')
    _defaults={
    	'logo':_get_logo
    }
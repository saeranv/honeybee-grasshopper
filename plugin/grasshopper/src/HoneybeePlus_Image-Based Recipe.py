# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Image-based Recipe.

-

    Args:
        _sky: A radiance sky. Find honeybee skies under 02::Daylight::Light Sources.
        _views: A list of honeybee views. Use view components under 00::create
            to create a view.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _radiancePar_: Radiance parameters for Grid-based analysis. Find Radiance
            parameters node under 03::Daylight::Recipes.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Grid-based analysis recipe. Connect this recipe to
            Run Radiance Analysis to run a grid-based analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Image-Based Recipe"
ghenv.Component.NickName = 'imageBasedRecipe'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from honeybee.radiance.recipe.pointintime.imagebased import ImageBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _sky and _views:
    # set a sunlight hours analysis recipe together if there are points
    analysisRecipe = ImageBased(_sky, _views, _analysisType_, _radiancePar_)
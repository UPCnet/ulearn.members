from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class UlearnmembersLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ulearn.members
        xmlconfig.file(
            'configure.zcml',
            ulearn.members,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ulearn.members:default')

ULEARN_MEMBERS_FIXTURE = UlearnmembersLayer()
ULEARN_MEMBERS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ULEARN_MEMBERS_FIXTURE,),
    name="UlearnmembersLayer:Integration"
)
ULEARN_MEMBERS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ULEARN_MEMBERS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="UlearnmembersLayer:Functional"
)

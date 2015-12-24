# -*- encoding: utf-8 -*-


class ActivationKey(object):
    """Manipulates Katello's activation-key."""
    command_base = 'activation-key'

    @classmethod
    def add_host_collection(cls, options=None):
        """Associate a resource"""
        cls.command_sub = 'add-host-collection'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_subscription(cls, options=None):
        """Add subscription"""
        cls.command_sub = 'add-subscription'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def content_override(cls, options=None):
        """Override product content defaults"""
        cls.command_sub = 'content-override'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def copy(cls, options=None):
        """Copy an activation key"""
        cls.command_sub = 'copy'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def host_collection(cls, options=None):
        """List associated host collections"""
        cls.command_sub = 'host-collections'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def product_content(cls, options=None):
        """List associated products"""
        cls.command_sub = 'product-content'
        return cls.execute(
            cls._construct_command(options),
            output_format='csv'
        )

    @classmethod
    def remove_host_collection(cls, options=None):
        """Remove the associated resource"""
        cls.command_sub = 'remove-host-collection'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_repository(cls, options=None):
        """Disassociate a resource"""
        cls.command_sub = 'remove-repository'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_subscription(cls, options=None):
        """Remove subscription"""
        cls.command_sub = 'remove-subscription'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def subscriptions(cls, options=None):
        """List associated subscriptions"""
        cls.command_sub = 'subscriptions'
        return cls.execute(cls._construct_command(options))


class Architecture(object):
    """
    Manipulates Foreman's architecture.
    """

    command_base = 'architecture'


class ComputeResource(object):
    """
    Manipulates Foreman's compute resources.
    """

    command_base = 'compute-resource'


class ContentHost(object):
    """Manipulates Katello engine's content-host command."""
    command_base = 'content-host'

    @classmethod
    def errata_apply(cls, options):
        """Schedule errata for installation"""
        cls.command_sub = 'errata apply'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def errata_info(cls, options):
        """Retrieve a single errata for a system"""
        cls.command_sub = 'errata info'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def errata_list(cls, options):
        """List errata available for the content host."""
        cls.command_sub = 'errata list'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_install(cls, options):
        """Install packages remotely."""
        cls.command_sub = 'package install'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_remove(cls, options):
        """Uninstall packages remotely."""
        cls.command_sub = 'package remove'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_upgrade(cls, options):
        """Update packages remotely."""
        cls.command_sub = 'package upgrade'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_upgrade_all(cls, options):
        """Update all packages remotely."""
        cls.command_sub = 'package upgrade-all'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_group_install(cls, options):
        """Install package groups remotely."""
        cls.command_sub = 'package-group install'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def package_group_remove(cls, options):
        """Uninstall package groups remotely."""
        cls.command_sub = 'package-group remove'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def tasks(cls, options=None):
        """Lists async tasks for a content host."""
        cls.command_sub = 'tasks'
        return cls.execute(
            cls._construct_command(options), output_format='csv')


class ContentView(object):
    """Manipulates Foreman's content view."""

    command_base = 'content-view'

    @classmethod
    def add_repository(cls, options):
        """Associate repository to a selected CV."""
        cls.command_sub = 'add-repository'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def add_version(cls, options):
        """Associate version to a selected CV."""
        cls.command_sub = 'add-version'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def publish(cls, options, timeout=None):
        """Publishes a new version of content-view."""
        cls.command_sub = 'publish'
        # Publishing can take a while so try to wait a bit longer
        if timeout is None:
            timeout = 120
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
            timeout=timeout,
        )

    @classmethod
    def version_info(cls, options):
        """Provides version info related to content-view's version."""
        cls.command_sub = 'version info'

        if options is None:
            options = {}

        return hammer.parse_info(cls.execute(cls._construct_command(options)))

    @classmethod
    def version_incremental_update(cls, options):
        """Performs incremental update of the content-view's version"""
        cls.command_sub = 'version incremental-update'
        if options is None:
            options = {}
            return cls.execute(
                cls._construct_command(options),
                output_format='info'
            )

    @classmethod
    def puppet_module_add(cls, options):
        """Associate puppet_module to selected CV"""
        cls.command_sub = 'puppet-module add'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def puppet_module_info(cls, options):
        """Provides puppet-module info related to content-view's version."""
        cls.command_sub = 'puppet-module info'

        if options is None:
            options = {}

        return hammer.parse_info(cls.execute(cls._construct_command(options)))

    @classmethod
    def filter_info(cls, options):
        """Provides filter info related to content-view's version."""

        cls.command_sub = 'filter info'

        if options is None:
            options = {}

        return hammer.parse_info(cls.execute(cls._construct_command(options)))

    @classmethod
    def filter_create(cls, options):
        """Add new filter to content view entity.

        Usage::

            hammer content-view filter create [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME    Content view name
            --content-view-id CONTENT_VIEW_ID   Content view numeric identifier
            --description DESCRIPTION           Description of the filter
            --inclusion INCLUSION               Specifies if content should be
                                                included or excluded, default:
                                                inclusion=false (One of yes/no,
                                                1/0, true/false)
            --name NAME                         name of the filter
            --organization ORGANIZATION_NAME    Organization name to search by
            --organization-id ORGANIZATION_ID   Organization ID
            --organization-label ORGANIZATION_LABEL   Organization label to
                                                      search by
            --original-packages ORIGINAL_PACKAGES     Add all packages without
                                                      Errata to the included/
                                                      excluded list. (Package
                                                      Filter only)
            --repositories REPOSITORY_NAMES      Comma separated list of values
            --repository-ids REPOSITORY_IDS      Repository ID
            --type TYPE                          type of filter (e.g. rpm,
                                                 package_group, erratum)

        """
        cls.command_sub = 'filter create'
        if options is None:
            options = {}
        return cls.execute(cls._construct_command(options))

    @classmethod
    def filter_update(cls, options):
        """Update existing content view filter entity.

        Usage::

            hammer content-view filter update [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME    Content view name
            --content-view-id CONTENT_VIEW_ID   Content view numeric identifier
            --id ID                             filter identifier
            --inclusion INCLUSION               Specifies if content should be
                                                included or excluded, default:
                                                inclusion=false (One of yes/no,
                                                1/0, true/false)
            --name NAME                         Name to search by
            --new-name NEW_NAME                 new name for the filter
            --organization ORGANIZATION_NAME    Organization name to search by
            --organization-id ORGANIZATION_ID   Organization ID
            --organization-label ORGANIZATION_LABEL   Organization label to
                                                      search by
            --original-packages ORIGINAL_PACKAGES     Add all packages without
                                                      Errata to the included/
                                                      excluded list. (Package
                                                      Filter only)
            --repositories REPOSITORY_NAMES      Repository Name
                                                 Comma separated list of values
            --repository-ids REPOSITORY_IDS      Repository ID
                                                 Comma separated list of values

        """
        cls.command_sub = 'filter update'
        if options is None:
            options = {}
        return cls.execute(cls._construct_command(options))

    @classmethod
    def filter_delete(cls, options):
        """Delete existing content view filter entity.

        Usage::

            hammer content-view filter delete [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME    Content view name
            --content-view-id CONTENT_VIEW_ID   Content view numeric identifier
            --id ID                             filter identifier
            --name NAME                         Name to search by
            --organization ORGANIZATION_NAME    Organization name to search by
            --organization-id ORGANIZATION_ID   Organization ID
            --organization-label ORGANIZATION_LABEL   Organization label to
                                                      search by

        """
        cls.command_sub = 'filter delete'
        if options is None:
            options = {}
        return cls.execute(cls._construct_command(options))

    @classmethod
    def filter_rule_create(cls, options):
        """Add new rule to content view filter."""
        cls.command_sub = 'filter rule create'
        if options is None:
            options = {}
        return cls.execute(cls._construct_command(options))

    @classmethod
    def version_list(cls, options):
        """Lists content-view's versions."""
        cls.command_sub = 'version list'
        if options is None:
            options = {}
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def version_promote(cls, options):
        """Promotes content-view version to next env."""
        cls.command_sub = 'version promote'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def version_delete(cls, options):
        """Removes content-view version."""
        cls.command_sub = 'version delete'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def remove_from_environment(cls, options=None):
        """Remove content-view from an environment"""
        cls.command_sub = 'remove-from-environment'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def remove(cls, options=None):
        """Remove versions and/or environments from a content view and
        reassign content hosts and keys

        """
        cls.command_sub = 'remove'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )


class DockerContainer(object):
    """Manipulates Docker containers."""
    command_base = 'docker container'

    @classmethod
    def create(cls, options=None):
        """Creates a docker container

        Usage::

            hammer docker container create [OPTIONS]

        Options::

            --attach-stderr ATTACH_STDERR             One of true/false,
                                                      yes/no, 1/0.
            --attach-stdin ATTACH_STDIN               One of true/false,
                                                      yes/no, 1/0.
            --attach-stdout ATTACH_STDOUT             One of true/false,
                                                      yes/no, 1/0.
            --capsule CAPSULE_NAME                    Name to search by
            --capsule-id CAPSULE_ID                   Id of the capsule
            --command COMMAND
            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --cpu-sets CPU_SETS
            --cpu-shares CPU_SHARES
            --entrypoint ENTRYPOINT
            --location-ids LOCATION_IDS               REPLACE locations with
                                                      given ids. Comma
                                                      separated list of values.
            --locations LOCATION_NAMES                Comma separated list of
                                                      values.
            --memory MEMORY
            --name NAME
            --organization-ids ORGANIZATION_IDS       REPLACE organizations
                                                      with given ids.  Comma
                                                      separated list of values.
            --organizations ORGANIZATION_NAMES        Comma separated list of
                                                      values.
            --registry-id REGISTRY_ID                 Registry this container
                                                      will have to use to get
                                                      the image
            --repository-name REPOSITORY_NAME         Name of the repository to
                                                      use to create the
                                                      container. e.g: centos
            --tag TAG                                 Tag to use to create the
                                                      container. e.g: latest
            --tty TTY                                 One of true/false,
                                                      yes/no, 1/0.

        """
        return super(DockerContainer, cls).create(options)

    @classmethod
    def delete(cls, options=None):
        """Deletes a docker container

        Usage::

            hammer docker container delete [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        return super(DockerContainer, cls).delete(options)

    @classmethod
    def info(cls, options=None):
        """Gets information about a docker container

        Usage::

            hammer docker container info [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        return super(DockerContainer, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """Lists docker containers

        Usage::

            hammer docker container list [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --page PAGE                               paginate results
            --per-page PER_PAGE                       number of entries per
                                                      request

        """
        return super(DockerContainer, cls).list(options)

    @classmethod
    def logs(cls, options=None):
        """Reads container logs

        Usage::

            hammer docker container logs [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by
            --stderr STDERR                           One of true/false,
                                                      yes/no, 1/0.
            --stdout STDOUT                           One of true/false,
                                                      yes/no, 1/0.
            --tail TAIL                               Number of lines to tail.
                                                      Default: 100

        """
        cls.command_sub = 'logs'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def start(cls, options=None):
        """Starts a docker container

        Usage::

            hammer docker container start [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'start'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def status(cls, options=None):
        """Gets the running status of a docker container

        Usage::

            hammer docker container status [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'status'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def stop(cls, options=None):
        """Stops a docker container

        Usage::

            hammer docker container stop [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'stop'
        return cls.execute(cls._construct_command(options))


class DockerImage(object):
    """Manipulates Docker images."""
    command_base = 'docker image'

    @classmethod
    def info(cls, options=None):
        """Gets information about docker images

        Usage::

            hammer docker image info [OPTIONS]

        Options::

            --id ID                       a docker image identifier
            --name NAME                   Name to search by
            --repository REPOSITORY_NAME  Repository name to search by
            --repository-id REPOSITORY_ID repository ID

        """
        return super(DockerImage, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """List docker images

        Usage::

            hammer docker image list [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME                    Content view
                                                                name
            --content-view-filter CONTENT_VIEW_FILTER_NAME      Name to search
                                                                by
            --content-view-filter-id CONTENT_VIEW_FILTER_ID     filter
                                                                identifier
            --content-view-id CONTENT_VIEW_ID                   content view
                                                                numeric
                                                                identifier
            --content-view-version CONTENT_VIEW_VERSION_VERSION Content view
                                                                version number
            --content-view-version-id CONTENT_VIEW_VERSION_ID   Content view
                                                                version
                                                                identifier
            --environment ENVIRONMENT_NAME                      Name to search
                                                                by
            --environment-id ENVIRONMENT_ID
            --organization ORGANIZATION_NAME                    Organization
                                                                name to search
                                                                by
            --organization-id ORGANIZATION_ID                   organization ID
            --organization-label ORGANIZATION_LABEL             Organization
                                                                label to search
                                                                by
            --product PRODUCT_NAME                              Product name to
                                                                search by
            --product-id PRODUCT_ID                             product numeric
                                                                identifier
            --repository REPOSITORY_NAME                        Repository name
                                                                to search by
            --repository-id REPOSITORY_ID                       repository ID

        """
        return super(DockerImage, cls).list(options, per_page)


class DockerRegistry(object):
    """Manipulates Docker registries."""
    command_base = 'docker registry'

    @classmethod
    def create(cls, options=None):
        """Creates a docker registry

        Usage::

            hammer docker registry create [OPTIONS]

        Options::

            --description DESCRIPTION
            --name NAME
            --password PASSWORD
            --url URL
            --username USERNAME

        """
        return super(DockerRegistry, cls).create(options)

    @classmethod
    def delete(cls, options=None):
        """Deletes a docker registry

        Usage::

            hammer docker registry delete [OPTIONS]

        Options::

            --id ID
            --name NAME                               Name to search by

        """
        return super(DockerRegistry, cls).delete(options)

    @classmethod
    def info(cls, options=None):
        """Gets information about docker registry

        Usage::

            hammer docker registry info [OPTIONS]

        Options::

            --id ID
            --name NAME                   Name to search by

        """
        return super(DockerRegistry, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """List docker registries

        Usage::

            hammer docker registry list [OPTIONS]

        Options::

            --order ORDER                 sort results
            --page PAGE                   paginate results
            --per-page PER_PAGE           number of entries per request
            --search SEARCH               filter results

        """
        return super(DockerRegistry, cls).list(options, per_page)

    @classmethod
    def update(cls, options=None):
        """Updates a docker registry

        Usage::

            hammer docker registry update [OPTIONS]

        Options::

            --description DESCRIPTION
            --id ID
            --name NAME                               Name to search by
            --new-name NEW_NAME
            --password PASSWORD
            --url URL
            --username USERNAME

        """
        return super(DockerRegistry, cls).update(options)


class DockerTag(object):
    """Manipulates Docker tags."""
    command_base = 'docker tag'

    @classmethod
    def info(cls, options=None):
        """Gets information about docker tags

        Usage::

            hammer docker tag info [OPTIONS]

        Options::

            --id ID                       a docker tag identifier
            --name NAME                   Name to search by
            --repository REPOSITORY_NAME  Repository name to search by
            --repository-id REPOSITORY_ID repository ID

        """
        return super(DockerTag, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """List docker tags

        Usage::

            hammer docker tag list [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME                    Content view
                                                                name
            --content-view-filter CONTENT_VIEW_FILTER_NAME      Name to search
                                                                by
            --content-view-filter-id CONTENT_VIEW_FILTER_ID     filter
                                                                identifier
            --content-view-id CONTENT_VIEW_ID                   content view
                                                                numeric
                                                                identifier
            --content-view-version CONTENT_VIEW_VERSION_VERSION Content view
                                                                version number
            --content-view-version-id CONTENT_VIEW_VERSION_ID   Content view
                                                                version
                                                                identifier
            --environment ENVIRONMENT_NAME                      Name to search
                                                                by
            --environment-id ENVIRONMENT_ID
            --organization ORGANIZATION_NAME                    Organization
                                                                name to search
                                                                by
            --organization-id ORGANIZATION_ID                   organization ID
            --organization-label ORGANIZATION_LABEL             Organization
                                                                label to search
                                                                by
            --product PRODUCT_NAME                              Product name to
                                                                search by
            --product-id PRODUCT_ID                             product numeric
                                                                identifier
            --repository REPOSITORY_NAME                        Repository name
                                                                to search by
            --repository-id REPOSITORY_ID                       repository ID

        """
        return super(DockerTag, cls).list(options, per_page)


class Docker(object):
    """Manipulates Docker images and tags."""
    command_base = 'docker'

    # Shortcuts to docker subcommands. Instead of importing each subcommand
    # class, import the Docker class and use it like this: Docker.image.list()
    container = DockerContainer
    image = DockerImage
    registry = DockerRegistry
    tag = DockerTag


class Domain(object):
    """
    Manipulates Foreman's domains.
    """

    command_base = 'domain'


class Environment(object):
    """Manipulates Foreman's environments."""

    command_base = 'environment'

    @classmethod
    def sc_params(cls, options=None):
        """List all smart class parameters."""
        cls.command_sub = 'sc-params'
        return cls.execute(cls._construct_command(options))


class Fact(object):
    """
    Searches Foreman's facts.
    """

    command_base = 'fact'


class GlobalParameter(object):
    """
    Manipulates Foreman's global parameters.
    """

    command_base = 'global-parameter'

    @classmethod
    def set(cls, options=None):
        """ Set global parameter """
        cls.command_sub = 'set'
        return cls.execute(cls._construct_command(options))


class GPGKey(object):
    """
    Manipulates Foreman's GPG Keys.
    """

    command_base = 'gpg'
    command_requires_org = True

    @classmethod
    def info(cls, options=None):
        """
        Gets information for GPG Key
        """

        cls.command_sub = 'info'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        # Need to rebuild the returned object
        # First check for content key
        # id, name, content, organization, repositories

        if len(result) > 0:

            # First item should contain most fields
            key_record = result.pop(0)
            if 'organization' not in key_record:
                raise ValueError('Could not find GPG Key')

            # Remaining items belong to content

            for item in result:
                for _, val in item.items():
                    key_record['content'] += val
            # Update result with dictionary
            result = key_record

        return result


class Host(object):
    """
    Manipulates Foreman's hosts.
    """

    command_base = 'host'

    @classmethod
    def facts(cls, options=None):
        """
        List all fact values.

        Usage:
            hammer host facts [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            --order ORDER                 sort results
            --page PAGE                   paginate results
            --per-page PER_PAGE           number of entries per request
            --search SEARCH               filter results
            -h, --help                    print help
        """
        cls.command_sub = 'facts'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        facts = []

        if result:
            facts = result

        return facts

    @classmethod
    def puppetrun(cls, options=None):
        """
        Force a puppet run on the agent.

        Usage:
            hammer host puppetrun [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            -h, --help                    print help
        """

        cls.command_sub = 'puppetrun'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def reboot(cls, options=None):
        """
        Reboot a host

        Usage:
            hammer host reboot [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            -h, --help                    print help
        """

        cls.command_sub = 'reboot'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def reports(cls, options=None):
        """
        List all reports.

        Usage:
            hammer host reports [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            --order ORDER                 sort results
            --page PAGE                   paginate results
            --per-page PER_PAGE           number of entries per request
            --search SEARCH               filter results
            -h, --help                    print help
        """

        cls.command_sub = 'reports'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        reports = []

        if result:
            reports = result

        return reports

    @classmethod
    def start(cls, options=None):
        """
        Power a host on

        Usage:
            hammer host start [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            -h, --help                    print help
        """

        cls.command_sub = 'start'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def status(cls, options=None):
        """
        Get status of host

        Usage:
            hammer host status [OPTIONS]

        Options:
            --id ID                       resource id
            --name NAME                   resource name
            -h, --help                    print help
        """

        cls.command_sub = 'status'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def stop(cls, options=None):
        """
        Power a host off

        Usage:
            hammer host stop [OPTIONS]

        Options:
            --force                       Force turning off a host
            --id ID                       resource id
            --name NAME                   resource name
            -h, --help                    print help
        """

        cls.command_sub = 'stop'

        result = cls.execute(cls._construct_command(options))

        return result


class HostCollection(object):
    """Manipulates Katello engine's host-collection command."""

    command_base = 'host-collection'

    @classmethod
    def add_content_host(cls, options=None):
        """Associate a content-host"""
        cls.command_sub = 'add-content-host'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_content_host(cls, options=None):
        """Remove a content-host"""
        cls.command_sub = 'remove-content-host'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def content_hosts(cls, options=None):
        """
        List content-hosts added to the host collection

        Usage::

            hammer host-collection content-hosts [OPTIONS]

        Options::

            --id ID                       Id of the host collection
            --name NAME                   Host collection name to search by
            --organization ORGANIZATION_NAME Organization name to search by
            --organization-id ORGANIZATION_ID
            --organization-label Organization label to search by
        """
        cls.command_sub = 'content-hosts'
        return cls.execute(
            cls._construct_command(options), output_format='csv')


class HostGroup(object):
    """
    Manipulates Foreman's hostgroups.
    """

    command_base = 'hostgroup'


class LifecycleEnvironment(object):
    """
    Manipulates Katello engine's lifecycle-environment command.
    """

    command_base = 'lifecycle-environment'
    command_requires_org = True

    @classmethod
    def list(cls, options=None, per_page=False):
        result = super(LifecycleEnvironment, cls).list(
            options, per_page=per_page)

        return result

    @classmethod
    def paths(cls, options=None):
        cls.command_sub = 'paths'
        return cls.execute(cls._construct_command(options))


class Location(object):
    """Manipulates Foreman's Locations"""

    command_base = 'location'

    @classmethod
    def add_compute_resource(cls, options=None):
        """Associate a compute resource"""

        cls.command_sub = 'add-compute-resource'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_config_template(cls, options=None):
        """Associate a configuration template"""

        cls.command_sub = 'add-config-template'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_domain(cls, options=None):
        """Associate a domain"""

        cls.command_sub = 'add-domain'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_environment(cls, options=None):
        """Associate an environment"""

        cls.command_sub = 'add-environment'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_hostgroup(cls, options=None):
        """Associate a hostgroup"""

        cls.command_sub = 'add-hostgroup'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_medium(cls, options=None):
        """Associate a medium"""

        cls.command_sub = 'add-medium'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_organization(cls, options=None):
        """Associate an organization"""

        cls.command_sub = 'add-organization'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_smart_proxy(cls, options=None):
        """Associate a smart proxy"""

        cls.command_sub = 'add-smart-proxy'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_subnet(cls, options=None):
        """Associate a subnet"""

        cls.command_sub = 'add-subnet'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_user(cls, options=None):
        """Associate a user"""

        cls.command_sub = 'add-user'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_compute_resource(cls, options=None):
        """Disassociate a compute resource"""

        cls.command_sub = 'remove-compute-resource'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_config_template(cls, options=None):
        """Disassociate a configuration template"""

        cls.command_sub = 'remove-config-template'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_domain(cls, options=None):
        """Disassociate a domain"""

        cls.command_sub = 'remove-domain'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_environment(cls, options=None):
        """Disassociate an environment"""

        cls.command_sub = 'remove-environment'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_hostgroup(cls, options=None):
        """Disassociate a hostgroup"""

        cls.command_sub = 'remove-hostgroup'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_medium(cls, options=None):
        """Disassociate a medium"""

        cls.command_sub = 'remove-medium'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_organization(cls, options=None):
        """Disassociate an organization"""

        cls.command_sub = 'remove-organization'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_smart_proxy(cls, options=None):
        """Disassociate a smart proxy"""

        cls.command_sub = 'remove-smart-proxy'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_subnet(cls, options=None):
        """Disassociate a subnet"""

        cls.command_sub = 'remove-subnet'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_user(cls, options=None):
        """Disassociate a user"""

        cls.command_sub = 'remove-user'

        return cls.execute(cls._construct_command(options))


class Medium(object):
    """
    Manipulates Foreman's installation media.
    """

    command_base = 'medium'


class Model(object):
    """
    Manipulates Foreman's hardware model.
    """

    command_base = 'model'


class OperatingSys(object):
    """
    Manipulates Foreman's operating systems.
    """

    command_base = 'os'

    @classmethod
    def add_architecture(cls, options=None):
        """
        Adds existing architecture to OS.
        """

        cls.command_sub = 'add-architecture'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def add_config_template(cls, options=None):
        """
        Adds existing template to OS.
        """

        cls.command_sub = 'add-config-template '

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def add_ptable(cls, options=None):
        """
        Adds existing partitioning table to OS.
        """

        cls.command_sub = 'add-ptable'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def remove_architecture(cls, options=None):
        """
        Removes architecture from OS.
        """

        cls.command_sub = 'remove-architecture'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def remove_config_template(cls, options=None):
        """
        Removes template from OS.
        """

        cls.command_sub = 'remove-config-template'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def remove_ptable(cls, options=None):
        """
        Removes partitioning table from OS.
        """

        cls.command_sub = 'remove-ptable '

        result = cls.execute(cls._construct_command(options))

        return result


class Org(object):
    """
    Manipulates Foreman's Organizations
    """

    command_base = 'organization'

    @classmethod
    def add_subnet(cls, options=None):
        """
        Adds existing subnet to an org
        """

        cls.command_sub = 'add-subnet'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_subnet(cls, options=None):
        """
        Removes a subnet from an org
        """

        cls.command_sub = 'remove-subnet'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_domain(cls, options=None):
        """
        Adds a domain to an org
        """

        cls.command_sub = 'add-domain'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_domain(cls, options=None):
        """
        Removes a domain from an org
        """

        cls.command_sub = 'remove-domain'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_user(cls, options=None):
        """
        Adds an user to an org
        """

        cls.command_sub = 'add-user'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_user(cls, options=None):
        """
        Removes an user from an org
        """

        cls.command_sub = 'remove-user'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_hostgroup(cls, options=None):
        """
        Adds a hostgroup to an org
        """

        cls.command_sub = 'add-hostgroup'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_hostgroup(cls, options=None):
        """
        Removes a hostgroup from an org
        """

        cls.command_sub = 'remove-hostgroup'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_compute_resource(cls, options=None):
        """
        Adds a computeresource to an org
        """

        cls.command_sub = 'add-compute-resource'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_compute_resource(cls, options=None):
        """
        Removes a computeresource from an org
        """

        cls.command_sub = 'remove-compute-resource'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_medium(cls, options=None):
        """
        Adds a medium to an org
        """

        cls.command_sub = 'add-medium'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_medium(cls, options=None):
        """
        Removes a medium from an org
        """

        cls.command_sub = 'remove-medium'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_config_template(cls, options=None):
        """
        Adds a configtemplate to an org
        """

        cls.command_sub = 'add-config-template'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_config_template(cls, options=None):
        """
        Removes a configtemplate from an org
        """

        cls.command_sub = 'remove-config-template'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_environment(cls, options=None):
        """
        Adds an environment to an org
        """

        cls.command_sub = 'add-environment'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_environment(cls, options=None):
        """
        Removes an environment from an org
        """

        cls.command_sub = 'remove-environment'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def add_smart_proxy(cls, options=None):
        """
        Adds a smartproxy to an org
        """

        cls.command_sub = 'add-smart-proxy'

        return cls.execute(cls._construct_command(options))

    @classmethod
    def remove_smart_proxy(cls, options=None):
        """
        Removes a smartproxy from an org
        """

        cls.command_sub = 'remove-smart-proxy'

        return cls.execute(cls._construct_command(options))


class PartitionTable(object):
    """
    Manipulates Foreman's partition tables.
    """

    command_base = 'partition-table'


class Product(object):
    """
    Manipulates Katello engine's product command.
    """

    command_base = 'product'
    command_requires_org = True

    @classmethod
    def remove_sync_plan(cls, options=None):
        """
        Delete assignment sync plan and product.
        """

        cls.command_sub = 'remove-sync-plan'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def set_sync_plan(cls, options=None):
        """
        Assign sync plan to product.
        """

        cls.command_sub = 'set-sync-plan'

        result = cls.execute(cls._construct_command(options))

        return result

    @classmethod
    def synchronize(cls, options=None):
        """Synchronize a product."""
        cls.command_sub = 'synchronize'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )


class Proxy(object):
    """Manipulates Foreman's smart proxies. """

    command_base = 'proxy'

    @classmethod
    def importclasses(cls, options=None):
        """Import puppet classes from puppet proxy."""
        cls.command_sub = 'import-classes'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def refresh_features(cls, options=None):
        """Refreshes smart proxy features"""
        cls.command_sub = 'refresh-features'
        return cls.execute(cls._construct_command(options))


class Puppet(object):
    """
    Search Foreman's puppet modules.
    """

    command_base = 'puppet-class'


class PuppetModule(object):
    """
    To list OR show puppet modules.
    """

    command_base = 'puppet-module'


class Report(object):
    """
    Manipulates Foreman's reports.
    """

    command_base = 'report'


class Repository(object):
    """
    Manipulates Katello engine's repository command.
    """

    command_base = 'repository'
    command_requires_org = True

    @classmethod
    def create(cls, options=None):
        cls.command_requires_org = False

        try:
            result = super(Repository, cls).create(options)
        finally:
            cls.command_requires_org = True

        return result

    @classmethod
    def info(cls, options=None):
        cls.command_requires_org = False

        try:
            result = super(Repository, cls).info(options)
        finally:
            cls.command_requires_org = True

        return result

    @classmethod
    def synchronize(cls, options, return_raw_response=None):
        """Synchronizes a repository."""
        cls.command_sub = 'synchronize'
        return cls.execute(
            cls._construct_command(options),
            output_format='csv',
            ignore_stderr=True,
            return_raw_response=return_raw_response,
        )

    @classmethod
    def upload_content(cls, options):
        """Upload content to repository."""
        cls.command_sub = 'upload-content'
        return cls.execute(
            cls._construct_command(options),
            output_format='csv',
            ignore_stderr=True,
        )


class RepositorySet(object):
    """
    Manipulates Katello engine's repository command.
    """

    command_base = 'repository-set'

    @classmethod
    def enable(cls, options):
        """Enables a repository."""
        cls.command_sub = 'enable'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def disable(cls, options):
        """Disables a repository."""
        cls.command_sub = 'disable'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def available_repositories(cls, options):
        """Lists the available repositories.

        hammer repository-set available-repositories --help

        Usage::

            hammer repository-set available-repositories [OPTIONS]

        Options::

            --id ID                                 ID of the repository set
            --name NAME                             Repository set
                                                    name to search by
            --organization ORGANIZATION_NAME        Organization
                                                    name to search by
            --organization-id ORGANIZATION_ID       organization ID
            --organization-label ORGANIZATION_LABEL Organization label
                                                    to search by
            --product PRODUCT_NAME                  Product name
                                                    to search by
            --product-id PRODUCT_ID                 product numeric identifier
            -h, --help                              print help

        """
        cls.command_sub = 'available-repositories'
        return cls.execute(
            cls._construct_command(options), output_format='csv')


class Role(object):
    """Manipulates Katello engine's role command."""

    command_base = 'role'


class SmartClassParameter(object):
    """
    Manipulates smart class parameters in Foreman
    """

    command_base = 'sc-param'


class Subnet(object):
    """
    Manipulates Foreman's subnets.
    """

    command_base = 'subnet'


class Subscription(object):
    """
    Manipulates Katello engine's subscription command.
    """

    command_base = 'subscription'

    @classmethod
    def upload(cls, options=None):
        """Upload a subscription manifest."""
        cls.command_sub = 'upload'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def delete_manifest(cls, options=None):
        """Deletes a subscription manifest."""
        cls.command_sub = 'delete-manifest'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def refresh_manifest(cls, options=None):
        """Refreshes a subscription manifest."""
        cls.command_sub = 'refresh-manifest'
        return cls.execute(
            cls._construct_command(options),
            ignore_stderr=True,
        )

    @classmethod
    def manifest_history(cls, options=None):
        """Provided history for subscription manifest"""
        cls.command_sub = 'manifest-history'
        return cls.execute(cls._construct_command(options))


class SyncPlan(object):
    """
    Manipulates Katello engine's sync-plan command.
    """

    command_base = 'sync-plan'
    command_requires_org = True

    @classmethod
    def create(cls, options=None):
        cls.command_requires_org = False

        try:
            result = super(SyncPlan, cls).create(options)
        finally:
            cls.command_requires_org = True

        return result

    @classmethod
    def info(cls, options=None):
        cls.command_requires_org = False

        try:
            result = super(SyncPlan, cls).info(options)
        finally:
            cls.command_requires_org = True

        return result


class Task(object):
    """
    Manipulates Foreman's task.
    """
    command_base = 'task'

    @classmethod
    def progress(cls, options=None):
        """Shows a task progress

        Usage::
            hammer task progress [OPTIONS]

        Options::
            --id ID                       UUID of the task
            --name NAME                   Name to search by
        """
        cls.command_sub = 'progress'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def resume(cls, options=None):
        """Resumes a task

        Usage:
            hammer task resume [OPTIONS]

        Options:
            --search SEARCH               Resume tasks matching search string
            --task-ids TASK_IDS           Comma separated list of values.
            --tasks TASK_NAMES            Comma separated list of values.
        """
        cls.command_sub = 'resume'
        return cls.execute(cls._construct_command(options))


class Template(object):
    """
    Manipulates Foreman's configuration templates.
    """

    command_base = 'template'

    @classmethod
    def kinds(cls, options=None):
        """
        Returns list of types of templates.
        """

        cls.command_sub = 'kinds'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        kinds = []

        if result:
            kinds = result

        return kinds

    @classmethod
    def add_operatingsystem(cls, options=None):
        """
        Adds operating system, requires "id" and "operatingsystem-id".
        """

        cls.command_sub = 'add-operatingsystem'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        return result

    @classmethod
    def remove_operatingsystem(cls, options=None):
        """
        Remove operating system, requires "id" and "operatingsystem-id".
        """

        cls.command_sub = 'remove-operatingsystem'

        result = cls.execute(
            cls._construct_command(options), output_format='csv')

        return result


class User(object):
    """
    Manipulates Foreman's users.
    """

    command_base = 'user'

    @classmethod
    def add_role(cls, options=None):
        """Add a role to a user."""
        cls.command_sub = 'add-role'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def remove_role(cls, options=None):
        """Remove a role from user."""
        cls.command_sub = 'remove-role'
        return cls.execute(
            cls._construct_command(options), output_format='csv')


class UserGroup(object):
    """Manipulates Foreman's user group."""

    command_base = 'user-group'

    @classmethod
    def add_role(cls, options=None):
        """Assign a user role.

        Usage:
            hammer user-group add-role [OPTIONS]

        Options:
            --id ID
            --name NAME                   Name to search by
            --role ROLE_NAME              User role name
            --role-id ROLE_ID
        """
        cls.command_sub = 'add-role'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def add_user(cls, options=None):
        """Associate an user.

        Usage:
            hammer user-group add-user [OPTIONS]

        Options:
            --id ID
            --name NAME                   Name to search by
            --user USER_LOGIN             User's login to search by
            --user-id USER_ID
        """
        cls.command_sub = 'add-user'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def add_user_group(cls, options=None):
        """Associate an user group.

        Usage:
            hammer user-group add-user-group [OPTIONS]

        Options:
            --id ID
            --name NAME                                   Name to search by
            --user-group, --usergroup USER_GROUP_NAME     Name to search by
            --user-group-id, --usergroup-id USER_GROUP_ID
        """
        cls.command_sub = 'add-user-group'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def remove_role(cls, options=None):
        """Remove a user role.

        Usage:
            hammer user-group remove-role [OPTIONS]

        Options:
            --id ID
            --name NAME                   Name to search by
            --role ROLE_NAME              User role name
            --role-id ROLE_ID
        """
        cls.command_sub = 'remove-role'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def remove_user(cls, options=None):
        """Disassociate an user.

        Usage:
            hammer user-group remove-user [OPTIONS]

        Options:
            --id ID
            --name NAME                   Name to search by
            --user USER_LOGIN             User's login to search by
            --user-id USER_ID
        """
        cls.command_sub = 'remove-user'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

    @classmethod
    def remove_user_group(cls, options=None):
        """Disassociate an user group.

        Usage:
            hammer user-group remove-user-group [OPTIONS]

        Options:
            --id ID
            --name NAME                                   Name to search by
            --user-group, --usergroup USER_GROUP_NAME     Name to search by
            --user-group-id, --usergroup-id USER_GROUP_ID
        """
        cls.command_sub = 'remove-user-group'
        return cls.execute(
            cls._construct_command(options), output_format='csv')


class UserGroupExternal(object):
    """Manages Foreman external user groups.

    Usage:
        hammer user-group external [OPTIONS] SUBCOMMAND [ARG] ...

    Subcommands:
        create         Create an external user group linked to a user group
        delete         Delete an external user group
        info           Show an external user group for user group
        list           List all external user groups for user group
        refresh        Refresh external user group
        update         Update external user group
    """
    command_base = 'user-group external'

    @classmethod
    def refresh(cls, options=None):
        cls.command_sub = 'refresh'
        return cls.execute(
            cls._construct_command(options), output_format='csv')

from .main import ExtraTorrent


def autoload():
    return ExtraTorrent()

config = [{
    'name': 'extratorrent',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'ExtraTorrent',
            'description': 'See <a href="http://extratorrent.cc/">extratorrent.cc</a>',
            'wizard': False,
			'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACL0lEQVR4AS1SPW/UQBAd23fxne/Ld2dvzvHuzPocEBAKokCBqGiQ6IgACYmvUKRBFEQgKKGg4BAlUoggggYUEQpSHOI7CIEoQs/fYcbLaU/efTvvvZlnA1qydoxU5kcxX0CkgmQZtPy0hCUjvK+WgEByOZ5dns1O5bzna8fRVkgsxH8B0YouIvBhdD5T11NiVOoKrsttyUcpRW0InUrFnwe9HzuP2uaQZYhF2LQ76TTXw2RVMTK8mYYbjfh+zNquMVCrqn93aArLSixPxnafdGDLaz1tjY5rmNa8z5BczEQOxQfCl1GyoqoWxYRN1bkh7ELw3q/vhP6HIL4TG9KumpjgvwuyM7OsjSj98E/vszMfZ7xvPtMaWxGO5crwIumKCR5HxDtJ0AWKGG204RfUd/3smJYqwem/Q7BTS1ZGfM4LNpVwuKAz6cMeROst0S2EwNE7GjTehO2H3dxqIpdkydat15G3F8SXBi4GlpBNlSz012L/k2+W0CLLk/jbcf13rf41yJeMQ8QWUZiHCfCA9ad+81nEKPtoS9mJOf9v0NmMJHgUT6xayheK9EIK7JJeU/AF4scDF7Y5SPlJrRcxJ+um4ibNEdObxLiIwJim+eT2AL5D9CIcnZ5zvSJi9eIlNHVVtZ831dk5svPgvjPWTq+ktWkd/kD0qtm71x+sDQe3kt6DXnM7Ct+GajmTxKlkAokWljyAKSm5oWa2w+BH4P2UuVub7eTyiGOQYapY/wEztHduSDYz5gAAAABJRU5ErkJggg==',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': True,
                },
                {
                    'name': 'domain',
                    'advanced': True,
                    'label': 'Proxy server',
                    'description': 'Domain for requests, keep empty to let CouchPotato pick.',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        }
    ]
}]

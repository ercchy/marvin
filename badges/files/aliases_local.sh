alias dev_install='ansible-playbook -i inventory/hosts --private-key=~/.vagrant.d/insecure_private_key -u vagrant -e "host=dev user=vagrant" install.yml'

function dev_restore() {
    ansible-playbook -i inventory/hosts --private-key=~/.vagrant.d/insecure_private_key -u vagrant -e "host=dev user=vagrant archive=$0" restore_from_s3.yml
}
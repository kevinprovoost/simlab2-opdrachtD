---
# This playbook will manage the users on the Pi of Ben

- name: User Management
  hosts: pi
  remote_user: kevin
  become: true